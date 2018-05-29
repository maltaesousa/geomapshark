from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from .models import PermitRequest
from .forms import PermitRequestForm

def index(request):
    return render(request, 'gpf/index.html', {})

def edit(request):
    # fouille = get_object_or_404(PermitRequest, pk=12)
    # PermisFouilleFormSet = modelformset_factory(PermitRequest, fields=('objectid', 'geom'))

    if request.method == 'POST':
        formset = PermitRequestForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = PermitRequestForm()
    return render(request, 'gpf/edit.html', {'formset': formset})
