from django.urls import path
from calculators import views

urlpatterns = [
    path('calculator/<int:num1>/<int:num2>/', views.calculator),
]