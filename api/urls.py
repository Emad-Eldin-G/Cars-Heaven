from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns =[ 
    path("Cars", views.All_Cars.as_view()),
    path("Cars/<int:pk>", views.Specific_Cars.as_view(), name="Specific"),
    path("Cars/<str:brand>", views.Brand.as_view()),

]

urlpatterns += staticfiles_urlpatterns()