"""ctf_bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from blog import views as blog_views
from user_auth import views as user_auth_views
from ctf_bank import views as ctf_bank_views
from account import views as account_views
from gift_card import views as gift_card_views
from django.contrib.auth.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/id/([0-9]+)', blog_views.show_entry, name='show_entry'),
    #url(r'^login/$', user_auth_views.user_login, name='user_login'),
    url(r'^login/$', auth_views.login, {'template_name': 'user_auth/user_login.html'}, name='user_login'),
    url(r'^register/$', user_auth_views.register, name='registration'),
    url(r'^logout/$', logout, {'template_name': 'logged_out.html', 'next_page': '/'},
        name='logout'),
    url(r'^settings/password_change/$', user_auth_views.password_change, name='password_change'),
    url(r'^exchange/$', account_views.exchange, name='exchange'),
    url(r'^gift_card/$', gift_card_views.acquire_gift_card, name='gift_card'),
    url(r'^loan/$', account_views.loan_request, name='loan_request'),
    url(r'^loan/history/$', account_views.loan_history, name='loan_history'),
    url(r'^$', ctf_bank_views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
