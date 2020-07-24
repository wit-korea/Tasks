from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    print(request)
    return render(request,'hello.html',{'title':'hello','body':'world'})

def http_response(request):
    str1= 'hello2'
    str2 = 'django'
    return HttpResponse(str1 + str2)