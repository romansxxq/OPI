from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('media/<int:index>/', views.media_detail, name='media_detail'),
]

urlpatterns += router.urls