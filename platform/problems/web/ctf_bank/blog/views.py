from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from blog.models import Entry


@require_http_methods(["GET"])
def show_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    return render(request, 'blog/entry.html', {'entry': entry})