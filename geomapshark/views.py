from django.shortcuts import render
from . import settings
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    apps = []
    for app in settings.INSTALLED_APPS:
        if not app.startswith('django') and \
           not app.startswith('bootstrap'):
            apps.append(app)
    context = { 'apps': apps }
    return render(request, 'geomapshark/index.html', context)
