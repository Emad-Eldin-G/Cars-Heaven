from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns =[ 
    #General Car information
    path("Cars", views.All_Cars.as_view()),
    path("Cars/Brand/<brand>", views.Brand.as_view(), name="Brand"),
    path("Cars/Name/<name>", views.Specific_Car.as_view(), name="Specific"),

    #Car Speed
    path("Cars/Speed/Top", views.Top_Speed.as_view(), name="Top Speed"),
    path("Cars/Speed/Low", views.Low_Speed.as_view(), name="Low Speed"),

    #Car Type
    path("Cars/Type/Sedan", views.Type_Sedan.as_view(), name="Type Sedan"),
    path("Cars/Type/SUV", views.Type_SUV.as_view(), name="Type SUV"),
    path("Cars/Type/Sport", views.Type_Sport.as_view(), name="Type Sport"),
    path("Cars/Type/Hatchback", views.Type_Hatchback.as_view(), name="Type Hatchback"),

    #Cars Power/Fuel
    path("Cars/Power/Gas", views.Power_Gas.as_view(), name="Power Gas"),
    path("Cars/Power/Electric", views.Power_Electric.as_view(), name="Power Electric"),
    path("Cars/Power/Hybrid", views.Power_Hybrid.as_view(), name="Power Hybrid"),
    path("Cars/Power/Hydrogen", views.Power_Hydrogen.as_view(), name="Power Hydrogen"),

    #Cars year of make
    path("Cars/Year/<int:year>", views.Year_of_make.as_view(), name="Year"),

    #Cars Date Sort
    path("Cars/Year/Sort/Newest", views.Sort_Newest.as_view(), name="Sort Newest"),
    path("Cars/Year/Sort/Oldest", views.Sort_Oldest.as_view(), name="Sort Oldest"),


]

urlpatterns += staticfiles_urlpatterns()