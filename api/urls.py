from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns =[ 
    #General Car information
    path("", views.All_Cars.as_view()),
    path("Car/<brand>", views.Car_Brand.as_view(), name="Car Brand"),
    path("brands/all", views.All_brands.as_view(), name="All Brand"),
    path("Name/<name>", views.Specific_Car.as_view(), name="Specific"),

    #Car Speed
    path("Speed/Top", views.Top_Speed.as_view(), name="Top Speed"),
    path("Speed/Low", views.Low_Speed.as_view(), name="Low Speed"),

    #Car Type
    path("Type/Sedan", views.Type_Sedan.as_view(), name="Type Sedan"),
    path("Type/SUV", views.Type_SUV.as_view(), name="Type SUV"),
    path("Type/Sport", views.Type_Sport.as_view(), name="Type Sport"),
    path("Type/Hatchback", views.Type_Hatchback.as_view(), name="Type Hatchback"),

    # Power/Fuel
    path("Power/Gas", views.Power_Gas.as_view(), name="Power Gas"),
    path("Power/Electric", views.Power_Electric.as_view(), name="Power Electric"),
    path("Power/Hybrid", views.Power_Hybrid.as_view(), name="Power Hybrid"),
    path("Power/Hydrogen", views.Power_Hydrogen.as_view(), name="Power Hydrogen"),

    # year of make
    path("Year/<int:year>", views.Year_of_make.as_view(), name="Year"),

    # Date Sort
    path("Year/Sort/Newest", views.Sort_Newest.as_view(), name="Sort Newest"),
    path("Year/Sort/Oldest", views.Sort_Oldest.as_view(), name="Sort Oldest"),
    
    #Blog Section
    path("Blogs", views.All_blogs.as_view(), name="All blogs"),
    


]

urlpatterns += staticfiles_urlpatterns()