
from django.urls import path, include
from . import views

urlpatterns = [

    path('details/', views.display),
    path('sendemail/', views.mailing),
]
