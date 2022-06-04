from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name="home"),
    path('blog', views.blog, name="blog"),
    path('brands', views.brands, name="brands"),
    path('latest', views.NewTest)
    #path('brands/<str:brandname>', views.specific_brand, name="Specific_Brand"),

]

urlpatterns += staticfiles_urlpatterns()  



