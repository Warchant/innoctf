from account.models import Account, Currency


def base_extension(request):
    account_balance = []
    account_rub_balance = ''
    if request.user.is_authenticated:
        user_accounts = Account.objects.filter(user=request.user)
        if user_accounts:
            for account in user_accounts:
                currency_short_name = Currency.objects.get(id=account.currency.id).short_name
                if currency_short_name == 'RUB':
                    account_rub_balance = {'currency_name': 'RUB', 'balance': account.balance}
                account_balance.append((account.balance, currency_short_name))
    return {'account_balance': account_balance,
            'account_rub_balance': account_rub_balance}