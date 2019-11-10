from django.shortcuts import render
from django.http import HttpResponse
# from views.generic import View


def index(request):

    context = {'boldmessage':'python,java,javascript'}

    return render(request,'rango/index.html',context)


def about(request):
    return HttpResponse('this is about rango')