from django import forms
from account.models import Account, Currency
from models import GiftCard


class GiftCardForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(GiftCardForm, self).__init__(*args, **kwargs)
        self.fields['value'] = forms.ChoiceField(choices=[(card.id, card) for card in GiftCard.objects.all()])
        account_balance = []
        user_accounts = Account.objects.filter(user=user)
        for account in user_accounts:
            account_balance.append(('%s / %s: %s' %
                                    (user.username, Currency.objects.get(id=account.currency.id).short_name,
                                     account.balance),
                                    Currency.objects.get(id=account.currency.id).id))
        self.fields['account'] = forms.ChoiceField(
            choices=[(currency_id, value) for value, currency_id in account_balance])
    value = forms.ChoiceField()
    account = forms.ChoiceField()