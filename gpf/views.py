from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.http import HttpResponseRedirect,HttpResponse
from .models import PermitRequest, Actor
from .forms import PermitRequestForm

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
@method_decorator(decorators, name='dispatch')
class PermitListView(ListView):

    model = PermitRequest
    paginate_by = 15  # if pagination is desired
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
