from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('about/', views.about, name='about-page'),
    path('admin/', admin.site.urls),
    path('details/', views.details, name='details-view'),
    path('save_details', views.save_details, name='save-details'),
]

