from django.contrib import admin
from .models import BookReview, Genre, Message
# Register your models here.

admin.site.register(BookReview)
admin.site.register(Genre)
admin.site.register(Message)
