from django.shortcuts import render
from .models import User
from .models import Media
# Create your views here.
def home(request):
    user = User(first_name='Роман', last_name='Матвійчук', description='Student')
    media = Media(title='Зелений слоник', description='Сімейний фільм', rating=100, studio_name='SuperPuper')
    context = {
        'user': user,
        'media': media
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')