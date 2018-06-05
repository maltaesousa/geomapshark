from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from .filters import PermitRequestFilter
from .forms import AddPermitRequestForm, ChangePermitRequestForm, ActorForm
from .models import Actor, Archelogy, PermitRequest
from .tables import PermitRequestTable, PermitExportTable
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin, SingleTableView
from django_tables2.export.views import ExportMixin



import json


@login_required
def index(request):
    return render(request, 'gpf/index.html', {})


@login_required
def permitRequestAdd(request):
    if request.method == 'POST':
        form = AddPermitRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.has_archeology = archeo_checker(form.cleaned_data['geom'])
            # Gets the data before pushing it to database
            permitRequest = form.save(commit=False)
            # Add current user
            permitRequest.company = Actor.objects.get(user=request.user)
            # Save it in database
            permitRequest.save()
            return HttpResponseRedirect("/")
    else:
        form = AddPermitRequestForm()
    return render(request, 'gpf/edit.html', {'form': form})


@permission_required('gpf.change_permitrequest')
def permitRequestChange(request):
    if request.method == 'POST':
        form = ChangePermitRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.has_archeology = archeo_checker(form.cleaned_data['geom'])
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = ChangePermitRequestForm()
    return render(request, 'gpf/edit.html', {'form': form})


@permission_required('gpf.permitdetail')
def permitdetail(request, pk):

    try:
        permit_id = PermitRequest.objects.get(pk=pk)
    except PermitRequest.DoesNotExist:
        raise Http404("Cette demande n'existe pas")
    form = ChangePermitRequestForm()
    return render(request, 'gpf/edit.html', {'form': form})


def actorAddPopup(request):
    form = ActorForm(request.POST or None)

    if form.is_valid():
        instance = form.save()
        # changes the value of the '#id_actor'
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_actor");</script>' % (instance.pk, instance))
    return render(request, 'gpf/actor_form.html', {'form' : form})


def actorChangePopup(request, pk=None):
    instance = get_object_or_404(Actor, pk=pk)
    form = ActorForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_actor");</script>' % (instance.pk, instance))
    return render(request, "gpf/actor_form.html", {'form' : form})


@csrf_exempt
def get_actor_id(request):
    if request.is_ajax():
        actor_name = request.GET['actor_name']
        actor_id = Actor.objects.get(name=actor_name).id
        data = {'actor_id': actor_id,}
        return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse("/")


@method_decorator(login_required, name="dispatch")
class PermitRequestListView(SingleTableMixin, FilterView):
    paginate_by = 10
    table_class = PermitRequestTable
    model = PermitRequest
    template_name = 'gpf/list.html'

    filterset_class = PermitRequestFilter

class PermitExportView(ExportMixin, SingleTableView):
    table_class = PermitExportTable
    model = PermitRequest
    template_name = 'django_tables2/bootstrap.html'

def archeo_checker(geom):
    archeo_polygons= Archelogy.objects.filter(geom__intersects=geom)
    archeo_polygons_eca = []
    for polygon in archeo_polygons:
        archeo_polygons_eca.append(polygon.eca)

    has_archeology = False
    if len(archeo_polygons_eca) > 0:
        has_archeology = True

    return has_archeology
