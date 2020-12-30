import requests

from django.shortcuts import render, redirect

from BikePortal.forms import TicketForm, ChartSliderForm
from BikePortal.models import Ticket

weather_data_url = 'http://127.0.0.1:5000/forecast'
alerts_url = 'http://127.0.0.1:5000/alerts'
health_data_url = 'http://127.0.0.1:5000/health-stats'


def index(request):

    weather_request = requests.get(weather_data_url)
    weather_dict = weather_request.json()
    alerts_request = requests.get(alerts_url)
    alerts_dict = alerts_request.json()
    health_request = requests.get(health_data_url)
    health_dict = health_request.json()

    ticks = Ticket.objects.all().order_by('-priority').filter(done=False)

    context={'alerts':alerts_dict,
             'health':health_dict,
             'weather':weather_dict,
             'ticks': ticks}
    return render(request,'index.html',context)

def cycling_stats(request):

    weather_request = requests.get(weather_data_url)
    weather_dict = weather_request.json()
    alerts_request = requests.get(alerts_url)
    alerts_dict = alerts_request.json()
    health_request = requests.get(health_data_url)
    health_dict = health_request.json()

    context = {'alerts': alerts_dict,
               'health': health_dict,
               'weather': weather_dict
               }
    return render(request, 'cycling-stats.html', context)

def cycling_data(request):

    weather_dict = requests.get(weather_data_url).json()
    alerts_dict = requests.get(alerts_url).json()
    health_dict = requests.get(health_data_url).json()

    cycling_data_form = ChartSliderForm()
    city, start_date, end_date = ''

    if request.method == 'POST':
        cycling_data_form = ChartSliderForm(request.POST)
        if cycling_data_form.is_valid():
            city = cycling_data_form.city
            start_date = cycling_data_form.date_range_start
            end_date = cycling_data_form.date_range_end  #wonder is that will work....

        return redirect('/cycling-stats'),city,start_date,end_date

    cycling_chart_data_krk = requests.get(f'http://127.0.0.1:5000/'
                                      f'city={city}'
                                      f'&startdate={start_date}'
                                      f'&enddate={end_date}').json()

    cycling_stats_data_krk = requests.get(f'http://127.0.0.1:5000/'
                                      f'statistic&city={city}'
                                      f'&startdate={start_date}'
                                      f'&enddate={end_date}').json()

    cycling_chart_data_br = requests.get(f'http://127.0.0.1:5000/'
                                      f'city={city}'
                                      f'&startdate={start_date}'
                                      f'&enddate={end_date}').json()

    cycling_stats_data_br = requests.get(f'http://127.0.0.1:5000/'
                                      f'statistic&city={city}'
                                      f'&startdate={start_date}'
                                      f'&enddate={end_date}').json()

    context = {'alerts': alerts_dict,
               'health': health_dict,
               'weather': weather_dict,
               'cycling_stats_krk': cycling_stats_data_krk,
               'cycling_stats_br': cycling_stats_data_br,
               'cycling_charts_krk': cycling_chart_data_krk,
               'cycling_charts_br': cycling_chart_data_br,
               'form': cycling_data_form
               }

    return render(request, 'cycling-data.html', context)

def maintenance(request):

    weather_request = requests.get(weather_data_url)
    weather_dict = weather_request.json()
    alerts_request = requests.get(alerts_url)
    alerts_dict = alerts_request.json()
    health_request = requests.get(health_data_url)
    health_dict = health_request.json()
    ticks = Ticket.objects.all().order_by('-priority').filter(done=False)
    form = TicketForm()


    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()


        return redirect('/maintenance')

    context = {'alerts': alerts_dict,
               'health': health_dict,
               'weather': weather_dict,
               'ticks': ticks,
               'form': form
               }

    return render(request, 'maintenance.html', context)


