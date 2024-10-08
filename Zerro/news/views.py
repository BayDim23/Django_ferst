from django.shortcuts import render
from .models import News_post
from .forms import News_postForm



def home(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})

def create_news(request):
    error = ''
    if request.method == 'POST':
        form = News_postForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            error = 'Форма заполнена неверно'
    form = News_postForm()
    return render(request, 'news/add_news.html', {'form': form, 'error': error})
