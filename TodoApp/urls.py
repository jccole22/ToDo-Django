
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('mark_complete/<list_id>', views.mark_complete, name='mark_complete'),
    path('mark_incomplete/<list_id>', views.mark_incomplete, name='mark_incomplete'),
    path('edit/<list_id>', views.edit, name='edit'),
]