from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from blog.models import Entry


@require_http_methods(["GET"])
@login_required
def index(request):
    entries = Entry.objects.all()
    return render(request, 'index.html', {'entries': entries})