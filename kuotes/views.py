from django.shortcuts import render

from kuotes.models import Kuote


def index(request):
    context = {
        'recent_kuotes': Kuote.objects.all()[:5]
    }
    return render(request, 'index.html', context)
