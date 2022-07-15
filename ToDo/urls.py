
from django.contrib import admin
from django.urls import path, include
from TodoApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TodoApp.urls'))
]
