from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    genre = models.CharField(max_length=20)

class BookReview(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null = True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    book_title = models.CharField(max_length=50)
    review_title = models.CharField(max_length=50)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        ordering = ['-created']
        
        
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_review = models.ForeignKey(BookReview, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        ordering = ['-created']

    
    
    
    
    
    
        