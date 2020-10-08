from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return HttpResponse("about page")



def contact(request):
    return HttpResponse("contact us")



def tracker(request):
    return HttpResponse("track ur order")


def search(request):
    return HttpResponse("search here")


def productview(request):
    return HttpResponse("product info")


def checkout(request):
    return HttpResponse("checkourt here")