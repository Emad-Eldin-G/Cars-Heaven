from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name="home"),
    path('Latest', views.New, name="New"),
    path('<str:pk>', views.Car, name="Car"),
    path('Brands', views.Brands, name="Brands"),
    
]

urlpatterns += staticfiles_urlpatterns()