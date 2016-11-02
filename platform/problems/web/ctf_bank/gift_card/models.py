# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from account.models import Currency

class GiftCard(models.Model):
    value = models.IntegerField()
    text = models.CharField(max_length=200)
    currency = models.ForeignKey(Currency)

    def __unicode__(self):
        return "%s%s" % (self.value, self.currency)

class GiftCardUser(models.Model):
    card = models.ForeignKey(GiftCard)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return "Card: %s User: %s" % (self.card, self.user)