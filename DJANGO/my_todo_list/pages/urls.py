
# contains views and urls

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'indexpage'),
    path('about/', views.about, name = 'about'),
]