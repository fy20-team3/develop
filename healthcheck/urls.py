from django.urls import path

from . import views


app_name = 'healthcheck'
urlpatterns = [
    path('', views.healthcheck, name='healthcheck'),
]

