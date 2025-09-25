from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car

def index(requst):
    num_drivers =Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_car = Car.objectc.count()

    cotext = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_car": num_car,
        }
    return render(
        requst, "taxi/index.html", context=cotext
        )