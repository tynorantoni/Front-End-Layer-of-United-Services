from django.shortcuts import render


def index(request):
    return render(request,'index.html',context={})

def cycling_stats(request):
    pass

def cycling_data(request):
    pass

def maintenance(request):
    pass


