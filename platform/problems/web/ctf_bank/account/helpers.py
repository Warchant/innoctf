from __future__ import division
from models import ExchangeRate


def conversion_ratio(source_currency_id, dest_currency_id):
    exchange_rates = ExchangeRate.objects.all()
    return exchange_rates.get(currency_id=source_currency_id).rate / exchange_rates.get(currency_id=dest_currency_id).rate