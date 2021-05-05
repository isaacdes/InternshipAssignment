from django.urls import path
from .import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    # path('details', views.details, name='details')
    
]
