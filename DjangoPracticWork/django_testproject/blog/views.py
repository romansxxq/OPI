from django.shortcuts import get_object_or_404, render
from .models import User, Media, Comment
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

def media_detail(request, index):
    media = get_object_or_404(Media, pk=index)
    comments = Comment.objects.filter(media=media)
    context = {
        'media': media,
        'comments': comments
    }
    return render(request, 'blog/media_detail.html', context)