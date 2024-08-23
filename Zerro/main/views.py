from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")

def new(request):
    return HttpResponse("<h1>Я вас приветствую</h1>")

