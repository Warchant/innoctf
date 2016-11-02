# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Currency(models.Model):
    short_name = models.CharField(max_length=3)
    long_name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.short_name


class Account(models.Model):
    # user and currency together represent an unique account
    class Meta:
        unique_together = (('user', 'currency'),)

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    balance = models.DecimalField(max_digits=9, decimal_places=2)
    currency = models.ForeignKey(Currency)

    def __unicode__(self):
        return "%s / %s: %s" % (self.user, self.currency, self.balance)


class Transaction(models.Model):
    account_from = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="%(class)s_from_related")
    account_to = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="%(class)s_to_related", null=True)
    type = models.IntegerField()  # 1:EXCHANGE, 2:LOAN
    date = models.DateTimeField()
    status = models.IntegerField()  # 1:PENDING, 2:APPROVED, 3:DECLINED
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    message = models.CharField(max_length=2000, null=True)

    def __unicode__(self):
        return "%s -> %s | type: %s | status: %s" % (self.user_from, self.user_to, self.type, self.status)


class ExchangeRate(models.Model):
    currency = models.ForeignKey(Currency)
    rate = models.DecimalField(max_digits=6, decimal_places=2)

    def __unicode__(self):
        return "%s: %s" % (self.currency, self.rate)
