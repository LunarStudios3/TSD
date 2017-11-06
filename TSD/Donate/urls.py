from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^',views.email,name='donate'),
    url(r'^thanks/',views.thanks,name='thanks'),
]
