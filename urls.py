
from django.contrib import admin
from django.urls import path
from Bengkel_api.views import Bengkel_list

urlpatterns = [
    path('list/', Bengkel_list)
]

