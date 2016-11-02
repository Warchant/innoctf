from django.contrib import admin
from models import *

admin.site.register([Account, ExchangeRate, Currency, Transaction])