from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView
from demos.models import Post


def url_view(request):
    print("url_view()")
    return HttpResponse('<h1>url_view</h1>')
    #return JsonResponse({'code':'001', 'msg':'OK'})     #dictionary 형식의 data 들어가야함

def url_parameter_view(request, username):
    print('url_parameter_view()')
    print(f'username : {username}')
    print(f'request.GET : {request.GET}')  #quary parameter 값 받아오기
    return HttpResponse(username)

def function_view(request):
    print(f'request.method : {request.method}')
    if request.method == "GET":
        print(f'request.GET : {request.GET}')
    elif request.method == "POST":
        print(f'request.POST : {request.POST}')
    return render(request, 'view.html')


class class_view(ListView):
    model = Post
    template_name = 'cbn_view.html'
