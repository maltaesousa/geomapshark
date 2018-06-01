from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.http import HttpResponseRedirect,HttpResponse
from .models import Actor, Archelogy, PermitRequest
from .forms import PermitRequestForm
from .filters import PermitRequestFilter

from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator


@login_required
def index(request):
    return render(request, 'gpf/index.html', {})

@login_required
def edit(request):

    if request.method == 'POST':
        form = PermitRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.has_archeology = archeo_checker(form.cleaned_data['geom'])
            # Gets the data before pushing it to database
            permitRequest = form.save(commit=False)
            # Add current user
            permitRequest.company = Actor.objects.get(user=request.user)
            # Save it in database
            permitRequest.save()
            #TODO return to somewhere.
    else:
        form = PermitRequestForm()
    return render(request, 'gpf/edit.html', {'form': form})

#List of decorators for the class based view
decorators = [login_required, permission_required('gpf.change_permitrequest')]

#This is the way to decorate a class based view
@login_required
def listpermit(request):

    filter = PermitRequestFilter(request.GET, queryset=PermitRequest.objects.all())

    return render(request, 'gpf/listpermit.html', {'filter': filter})



def archeo_checker(geom):

    archeo_polygons= Archelogy.objects.filter(geom__intersects=geom)
    archeo_polygons_eca = []
    for polygon in archeo_polygons:
        archeo_polygons_eca.append(polygon.eca)

    has_archeology = False
    if len(archeo_polygons_eca) > 0:
        has_archeology = True

    return has_archeology
