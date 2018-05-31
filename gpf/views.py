from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.http import HttpResponseRedirect,HttpResponse
from .models import PermitRequest, Archelogy
from .forms import PermitRequestForm

from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@login_required
def index(request):
    return render(request, 'gpf/index.html', {})

@login_required
def edit(request):

    if request.method == 'POST':
        formset = PermitRequestForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.instance.has_archeology = archeo_checker(formset.cleaned_data['geom'])
            formset.save()

    else:
        formset = PermitRequestForm()
    return render(request, 'gpf/edit.html', {'formset': formset})

@method_decorator(login_required, name='dispatch')
class PermitListView(ListView):

    model = PermitRequest
    paginate_by = 15
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def archeo_checker(geom):

    archeo_polygons= Archelogy.objects.filter(geom__intersects=geom)
    archeo_polygons_eca = []
    for polygon in archeo_polygons:
        archeo_polygons_eca.append(polygon.eca)

    has_archeology = False
    if len(archeo_polygons_eca) > 0:
        has_archeology = True

    return has_archeology
