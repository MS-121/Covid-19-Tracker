from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="tracker-home"),
    path('country/', views.country, name='country-wise'),
    path('news/', views.news, name='news'),
    path('statewise/', views.statedata, name='statedata')
]