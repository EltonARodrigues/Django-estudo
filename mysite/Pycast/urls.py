from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'Pycast'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    
] 


