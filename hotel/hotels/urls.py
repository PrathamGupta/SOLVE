from django.conf.urls import url

from . import views 

app_name = 'hotels'
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^/makeCard/$', views.makeCard, name='makeCard'),
    url(r'^/addCard/$', views.addCard, name='addCard'),
    url(r'^/login/$', views.loginPage, name='loginPage'),
    url(r'^/register/$', views.register, name='register'),
]