from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name="home"),
    path('blog', views.blog, name="blog"),

]

urlpatterns += staticfiles_urlpatterns()