from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('save/',views.data_save, name='save'), 
    path('delete/',views.data_delete, name='delete'),
]
