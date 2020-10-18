from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    res = render(request,'index.html')
    return HttpResponse(res)