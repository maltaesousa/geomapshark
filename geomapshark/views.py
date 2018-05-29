from django.shortcuts import render
from . import settings

def index(request):
    apps = []
    for app in settings.INSTALLED_APPS:
        if not app.startswith('django.contrib'):
            apps.append(app)
    context = { 'apps': apps }
    return render(request, 'geomapshark/index.html', context)
