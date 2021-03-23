from django.urls import path
from .views import get_data

urlpatterns = [
    path('<str:text1>/<int:num1>/<str:text2>/<int:num2>/', get_data)
]