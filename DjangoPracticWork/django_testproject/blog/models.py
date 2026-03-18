from django.db import models
from dataclasses import dataclass
# Create your models here.
@dataclass
class User:
    first_name: str
    last_name: str
    description: str

@dataclass
class Media:
    title: str
    description: str
    rating: int
    studio_name: str

class Media(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.IntegerField()
    studio_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Comment(models.Model):
    media = models.OneToOneField(Media, on_delete=models.CASCADE, related_name='comment')
    text = models.TextField()

    def __str__(self):
        return f"Comment for {self.media.title}"