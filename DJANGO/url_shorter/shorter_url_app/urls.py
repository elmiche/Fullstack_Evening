
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'app-home'),
    path('/my_urls', views.url_strgen, name='my-urls')
]
# not sure how to do this next step: gett the url from the DB 
# perhaps this is where I need to use the redirect view, not HTML