from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('blog', views.blog, name="blog"),
    path('brands', views.brands, name="brands"),
    path('latest', views.NewTest),
    path('signup', views.Signup),

]

urlpatterns += staticfiles_urlpatterns()  



