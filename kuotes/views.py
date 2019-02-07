from django.shortcuts import render
from urllib import parse

from kuotes.models import Kuote


def _enrich(quote):
    quote.source.domain = parse.urlparse(quote.source.url).netloc
    return quote


def index(request):
    context = {
        'recent_kuotes': list(map(_enrich, Kuote.objects.all()[:5]))
    }
    return render(request, 'index.html', context)
