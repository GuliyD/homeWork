from django.shortcuts import render
from django.utils import translation
from .models import UserData


def get_data(request, text1, num1, text2, num2):
    UserData.objects.create(text1=text1, num1=num1, text2=text2, num2=num2)
    model = UserData.objects.all()
    return render(request, 'take_data/index.html', {'model': model})


def calculator(request, num1, num2, dz):
    if dz == 'plus':
        result = num1+num2
    if dz == 'minus':
        result = num1-num2
    if dz == 'iloczyn':
        result = num1*num2
    return render(request, 'take_data/calculator.html', {'result': result})

def get_info(request):
    user_agent = request.META.get('HTTP_USER_AGENT')
    language = translation.get_language()
    cookie = request.COOKIES
    host = request.META.get('HTTP_HOST')
    response = render(request, 'take_data/get_info.html', {'user_agent': user_agent, 'language': language, 'cookie': cookie, 'host': host}
                      )
    response.set_cookie('qwe', 'this is cookie')
    return response