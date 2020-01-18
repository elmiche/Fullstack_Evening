from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.create, name = 'app-home'),
    path('read-list/', views.read, name = 'read-list'), #creating the path to the read view, return the name 'read-list' in the view function!
    path('remove-item/<int:id>', views.remove, name = 'remove-item'),
    path('update/<int:id>', views.update, name ='update'),
    path('admin/', admin.site.urls),
]