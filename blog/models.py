from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    banner =models.ImageField(default="fallback.png", blank=True)
    created_by = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[str(self.id)])
    