from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.shortcuts import redirect
 
 
urlpatterns = [
        path('', lambda request: redirect('display/', permanent=False)),
         path('display/', views.display, name ='display'),
         path('add_pass/', views.add_pass, name ='add_pass'),
         path('delete_pass/', views.delete_pass, name ='delete_pass'),
         path('edit_pass/<id>/', views.edit_pass, name ='edit_pass'),
          path('register/', views.register, name ='register'),
          path('login/', views.Login, name ='login'),
]