from django.urls import path
from .import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
     path('create', views.create_user),
    # path('details', views.details, name='details')
    
]
