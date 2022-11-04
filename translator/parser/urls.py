from . import views
from django.urls import path

app_name = 'parser'

urlpatterns = [
    path('', views.home, name='home'),

]