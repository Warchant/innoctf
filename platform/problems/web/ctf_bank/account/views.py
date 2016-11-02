# -*- coding: utf-8 -*-
from __future__ import division
from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from models import ExchangeRate, Account, Transaction, Currency
from forms import CurrencyExchangeForm, LoanRequestForm
from django.db.models import F, Q
from django.db import transaction
from datetime import datetime
from helpers import conversion_ratio


@require_http_methods(["POST", "GET"])
@login_required
def exchange(request):
    exchange_rates = ExchangeRate.objects.all()
    exchange_rates_display = exchange_rates.exclude(currency__short_name='RUB')
    if request.method == 'POST':
        form = CurrencyExchangeForm(request.POST, user=request.user)
        if form.is_valid():
            conversion_rate = conversion_ratio(form.cleaned_data['from_acc'], form.cleaned_data['to_acc'])
            with transaction.atomic():
                Account.objects.filter(currency_id=form.cleaned_data['from_acc'], user=request.user).update(
                    balance=F('balance') - form.cleaned_data['amount'])
                # rounding problem
                Account.objects.filter(currency_id=form.cleaned_data['to_acc'], user=request.user).update(
                    balance=F('balance') + Decimal(round(form.cleaned_data['amount'] * Decimal(conversion_rate),0)))
                Transaction.objects.create(account_from=Account.objects.get(
                    user=request.user, currency_id=form.cleaned_data['from_acc']),
                    account_to=Account.objects.get(user=request.user, currency_id=form.cleaned_data['to_acc']), type=1,
                    date=datetime.now(), status=2, amount=form.cleaned_data['amount'])
    else:
        form = CurrencyExchangeForm(user=request.user)
    return render(request, 'exchange.html', {'form': form,
                                             'exchange_rates': exchange_rates_display})


@require_http_methods(["POST", "GET"])
@csrf_exempt
@login_required
def loan_request(request):
    if not request.user.is_staff:
        loans = Transaction.objects.filter(
            Q(account_from__exact=Account.objects.get(user=request.user,
                                                      currency=Currency.objects.get(short_name='RUB'))) |
            Q(account_from__exact=Account.objects.get(user=request.user,
                                                      currency=Currency.objects.get(short_name='RUB'))),
            type=2)
        if request.method == 'GET':
            form = LoanRequestForm()
        else:
            form = LoanRequestForm(request.POST)
            if form.is_valid():
                loan_requests = Transaction.objects.filter(Q(status__exact=1) | Q(status__exact=2),
                                                           account_from=Account.objects.get(user=request.user,
                                                                                            currency=Currency.objects.get(
                                                                                                short_name='RUB')),
                                                           type=2)  # loans in PENDING or APPROVED state
                loan_requests_amount = 0
                for loan_amount in loan_requests:
                    loan_requests_amount += loan_amount.amount
                    # limit loan to 1K RUB
                if form.cleaned_data['amount'] + loan_requests_amount <= 1000:
                    Transaction.objects.create(account_from=Account.objects.get(
                        user=request.user, currency=Currency.objects.get(short_name='RUB')), account_to=None, type=2,
                        date=datetime.now(), status=1, message=form.cleaned_data['message'], amount=form.cleaned_data['amount'])
                    messages.add_message(request, messages.SUCCESS, 'Запрос отправлен')
                else:
                    form.add_error(None, 'Превышен лимит на общую сумму займов (1000р)')
        return render(request, 'loan_request.html', {'form': form,
                                                     'loans': loans})
    else:
        loans = Transaction.objects.filter(type=2)
        if request.method == 'POST':
            loan_id = request.POST['loan_id']
            if Transaction.objects.get(id=loan_id).status == 1:
                if 'loan_approve' in request.POST:
                    Transaction.objects.filter(id=loan_id).update(status=2)
                    account_from = Transaction.objects.get(id=loan_id).account_from
                    Account.objects.filter(user=account_from.user, currency=Currency.objects.get(short_name='RUB')).update(
                        balance=F('balance') + Transaction.objects.get(id=loan_id).amount)
                elif 'loan_decline' in request.POST:
                    Transaction.objects.filter(id=loan_id).update(status=3)
        return render(request, 'loan_approve.html')


@require_http_methods(["GET"])
@login_required
def loan_history(request):
    loans = Transaction.objects.filter(
        Q(account_from__exact=Account.objects.get(user=request.user,
                                                  currency=Currency.objects.get(short_name='RUB'))) |
        Q(account_from__exact=Account.objects.get(user=request.user,
                                                  currency=Currency.objects.get(short_name='RUB'))),
        type=2)
    return render(request, 'loan_history.html', {'loans':loans})