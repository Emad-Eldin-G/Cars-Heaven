from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name="home"),
    path('Latest', views.New, name="New"),
    path('Brands', views.Brands , name='Brands'),
    path('<str:pk>', views.Car, name="Car"),

]

urlpatterns += staticfiles_urlpatterns()