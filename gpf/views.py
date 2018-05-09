from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from .models import PermisFouille,PermisFouilleForm
from django.forms import modelformset_factory

def index(request):
    return HttpResponse("Application de Gestion des Permis de Fouille")

# def edit(request):
#     fouille = get_object_or_404(PermisFouille, pk=12)
#     return render(request, 'gpf/edit.html', {'fouille': fouille})

def edit(request):
    # fouille = get_object_or_404(PermisFouille, pk=12)
    # PermisFouilleFormSet = modelformset_factory(PermisFouille, fields=('objectid', 'geom'))

    if request.method == 'POST':
        formset = PermisFouilleForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = PermisFouilleForm()
    return render(request, 'gpf/edit.html', {'formset': formset})
