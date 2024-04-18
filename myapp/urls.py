from django.urls import path
from . import views

urlpatterns = [
    path('oee/<int:machine_id>/', views.calculate_oee),
]
