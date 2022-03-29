from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns =[ 
    path("Cars", views.All_Cars.as_view()),
    path("Cars/Brand/<brand>", views.Brand.as_view(), name="Brand"),
    path("Cars/Name/<name>", views.Specific_Car.as_view(), name="Specific"),
    path("Cars/Speed/Top", views.Top_Speed.as_view(), name="Top Speed"),

]

urlpatterns += staticfiles_urlpatterns()