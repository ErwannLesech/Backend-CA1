from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Motorcycle, Description


def index(request):
    latest_motorcycle_list = Motorcycle.objects.order_by('-pub_date')[:5]
    context = {'latest_motorcycle_list': latest_motorcycle_list}
    return render(request, 'garage/index.html', context)

    def get_queryset(self):
        """Return the last five published motorcycles."""
        return Motorcycle.objects.order_by('-pub_date')[:5]



def description(request, motorcycle_id):
    motorcycle = get_object_or_404(Motorcycle, pk=motorcycle_id)
    return render(request, 'garage/description.html', {'motorcycle': motorcycle})

