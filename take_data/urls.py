from django.urls import path
from .views import get_data, calculator, get_info

urlpatterns = [
    path('<str:text1>/<int:num1>/<str:text2>/<int:num2>/', get_data),
    path('calculator/<int:num1>/<int:num2>/<str:dz>', calculator),
    path('get_info', get_info)
]