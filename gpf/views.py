from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.http import HttpResponseRedirect,HttpResponse
from .models import PermitRequest
from .forms import PermitRequestForm

from django.views.generic.list import ListView


def index(request):
    return render(request, 'gpf/index.html', {})


def edit(request):

    # fouille = get_object_or_404(PermitRequest, pk=12)

    if request.method == 'POST':
        formset = PermitRequestForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = PermitRequestForm()
    return render(request, 'gpf/edit.html', {'formset': formset})

class PermitListView(ListView):

    model = PermitRequest
    paginate_by = 15  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
