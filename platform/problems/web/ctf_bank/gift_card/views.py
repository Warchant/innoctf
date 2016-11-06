# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from forms import *
from account.models import Account
from gift_card.models import GiftCardUser
from account.helpers import conversion_ratio


@require_http_methods(["POST", "GET"])
@login_required
def acquire_gift_card(request):
    user_gift_cards = GiftCardUser.objects.filter(user=request.user)
    if request.method == 'GET':
        form = GiftCardForm(user=request.user)
    else:
        form = GiftCardForm(request.user, request.POST)
        if form.is_valid():
            user_balance = Account.objects.get(user=request.user, currency_id=form.cleaned_data['account']).balance
            gift_card = GiftCard.objects.get(id=form.cleaned_data['value'])
            gift_card_converted_cost = conversion_ratio(gift_card.currency_id, form.cleaned_data['account']) * \
                                       gift_card.value
            if user_balance >= gift_card_converted_cost:
                Account.objects.filter(currency_id=form.cleaned_data['account'], user=request.user).update(
                    balance=F('balance') - gift_card_converted_cost)
                GiftCardUser.objects.create(card=gift_card, user=request.user)
            else:
                form.add_error(None, 'Недостаточно средств на счёте')

    return render(request, 'gift_card.html', {'form': form,
                                              'user_gift_cards': user_gift_cards})
