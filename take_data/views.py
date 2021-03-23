from django.shortcuts import render

from .models import UserData


def get_data(request, text1, num1, text2, num2):
    UserData.objects.create(text1=text1, num1=num1, text2=text2, num2=num2)
    model = UserData.objects.all()
    return render(request, 'take_data/index.html', {'model': model})