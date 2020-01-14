
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'app-home'),
    path('my-urls/', views.url_list, name='my-urls'),
    # path('VLzu8', views.url_redirect, name='url-redirect'),
    path('<slug:shorty>', views.url_redirect, name='url-redirect')
]
# not sure how to do this next step: gett the url from the DB 
# perhaps this is where I need to use the redirect view, not HTML