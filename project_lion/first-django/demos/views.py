from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. 비즈니스로직 처리 기능, 작동
def calculator(request):
    #return HttpResponse("계산기 기능 구현 시작입니다.")
    return render(request, 'calculator.html')