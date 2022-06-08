from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def calculator(request):
    #return HttpResponse("계산기 기능 구현")
    print(f'request = {request}')
    print(f'request type = {type(request)}')
    print(f'requset.__dict__ = {request.__dict__}')

    #1. 데이터 확인
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operator = request.GET.get('operator')

    #2. 계산
    if operator  == '+':
        result = int(num1) + int(num2)
    elif operator == '-':
        result = int(num1) - int(num2)
    elif operator == '*':
        result = int(num1) * int(num2)
    elif operator == '/':
        result = int(num1) / int(num2)
    else:
        result = 0

    #3. 응답
    return render(request, 'calculator.html', {'result' : result})

def lotto(request):
    import random

    #1~45의 정수가 담긴 list 생성
    num = list(range(1,46))

    #num list 중에 6개의 정수 랜덤으로 뽑기
    lotto_num = random.sample(num,6)

    #응답
    return render(request, 'lotto.html',{'lotto_num' : lotto_num})