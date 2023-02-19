from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Motorcycle
from .forms import CreateNewMotorcycle


def index(request):
    latest_motorcycle_list = Motorcycle.objects.order_by('-pub_date')[:5]
    context = {'latest_motorcycle_list': latest_motorcycle_list}
    return render(request, 'garage/index.html', context)


def description(request, motorcycle_id):
    motorcycle = get_object_or_404(Motorcycle, pk=motorcycle_id)
    return render(request, 'garage/description.html', {'motorcycle': motorcycle})


def create(request):    
    if request.method == "POST":
        form = CreateNewMotorcycle(request.POST)
        # save the new motorcycle to the database:
        if form.is_valid():
            name = form.cleaned_data["motorcycle_text"]
            description = form.cleaned_data["motorcycle_description"]
            brand = form.cleaned_data["motorcycle_brand"]
            time = form.cleaned_data["pub_date"]
            Motorcycle.objects.create(motorcycle_text=name, motorcycle_brand=brand, motorcycle_description=description, pub_date=time)
        return render(request, 'garage/create.html', {'form': form})
    else:
        form = CreateNewMotorcycle()
    return render(request, 'garage/create.html', {'form': form})

