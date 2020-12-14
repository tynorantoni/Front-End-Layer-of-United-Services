from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cycling-stats', views.cycling_stats, name='cycling_stats'),
    path('cycling-data', views.cycling_data, name='cycling_data'),
    path('maintenance', views.maintenance, name='maintenance'),
]