

from django.urls import path
from . import views

urlpatterns = [
    path('',views.create_url),
    path('myapi/',views.api),
    path('myapi/',views.api),
    path('<slug:key>/',views.routetoURL),
    
]
