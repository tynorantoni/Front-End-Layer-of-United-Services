from django.shortcuts import render, redirect

from BikePortal.forms import TicketForm
from BikePortal.models import Ticket
from .weatherhandler import WeatherHandler


def index(request):
    # pogoda = WeatherHandler().get_weather_data()
    ticks = Ticket.objects.all().order_by('-priority').filter(done=False)
    alerts={}
    health={'bss':'alive','kss':'dead'}
    context={'alerts':alerts,
             'health':health,
             'ticks': ticks}
    return render(request,'index.html',context)

def cycling_stats(request):
    alerts = {}
    context = {'alerts': alerts}
    return render(request, 'cycling-stats.html', context)

def cycling_data(request):
    alerts = {}
    context = {'alerts': alerts}
    return render(request, 'cycling-data.html', context)

def maintenance(request):
    ticks = Ticket.objects.all().order_by('-priority').filter(done=False)
    form = TicketForm()


    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()


        return redirect('/')



    alerts = {}
    context = {'alerts': alerts,
               'ticks': ticks,
               'form': form
               }
    return render(request, 'maintenance.html', context)


