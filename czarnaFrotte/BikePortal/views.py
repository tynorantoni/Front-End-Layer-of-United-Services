from django.shortcuts import render


def index(request):
    alerts={}
    health={'bss':'alive','kss':'dead'}
    context={'alerts':alerts,
             'health':health}
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
    alerts = {}
    context = {'alerts': alerts}
    return render(request, 'maintenance.html', context)


