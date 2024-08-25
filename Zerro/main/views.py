from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'main/index.html')

def new(request):
    return render(request, 'main/new.html')
def m(request):
    return render(request, 'main/m.html')

def s(request):
    return render(request, 'main/file/s.html')

def f(request):
    return render(request, 'main/file/f.html')

def g(request):
    return render(request, 'main/file/g.html')

