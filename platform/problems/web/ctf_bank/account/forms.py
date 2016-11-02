# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError

from models import Account, Currency, ExchangeRate


class CurrencyExchangeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CurrencyExchangeForm, self).__init__(*args, **kwargs)
        account_balance = []
        user_accounts = Account.objects.filter(user=self.user)
        for account in user_accounts:
            account_balance.append(('%s / %s: %s' %
                                    (self.user.username, Currency.objects.get(id=account.currency.id).short_name, account.balance),
                                    Currency.objects.get(id=account.currency.id).id))
        self.fields['from_acc'] = forms.ChoiceField(
            choices=[(currency_id, value) for value, currency_id in account_balance])
        self.fields['to_acc'] = forms.ChoiceField(
            choices=[(currency_id, value) for value, currency_id in account_balance])

    def clean(self):
        cleaned_data = super(CurrencyExchangeForm, self).clean()
        # same accounts
        if cleaned_data.get('from_acc') == cleaned_data.get('to_acc'):
            raise ValidationError('Невозможно перевести на счет с таким же номером')
        # minimal amount
        minimal_amount = 60  # roubles
        ex_rates = ExchangeRate.objects.get(currency_id=cleaned_data.get('from_acc'))
        if cleaned_data.get('amount') * ex_rates.rate < minimal_amount:
            raise ValidationError('Сумма конвертации должна быть не меньше %sр или эквивалент в валюте'
                                      % minimal_amount)
        # not existing currency ID
        if int((cleaned_data.get('from_acc')) or int(cleaned_data.get('to_acc'))) not in \
                Currency.objects.all().values_list('id', flat=True):
            raise ValidationError('Валюты с таким ID не существует')
        user_balance = Account.objects.get(currency_id=cleaned_data.get('from_acc'), user=self.user).balance
        if user_balance < cleaned_data.get('amount'):
            raise ValidationError('Сумма на счету меньше конвертируемой')

    from_acc = forms.ChoiceField()
    to_acc = forms.ChoiceField()
    amount = forms.DecimalField()


class LoanRequestForm(forms.Form):
    amount = forms.DecimalField(max_value=1000)
    message = forms.CharField(widget=forms.Textarea)

