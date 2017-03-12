from django.conf.urls import url
from . import views

urlpatterns = [url(r'^images$', views.image_list, name = ' image_list'),]