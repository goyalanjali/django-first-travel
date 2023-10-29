from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name' : 'Anjali'})
   # return HttpResponse("Hello World")


def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2

    return render(request, 'result.html', {'result' : res})   


@api_view()
def appi(request):
    return response({'name': 'anjali', 'status': 'han'})


   