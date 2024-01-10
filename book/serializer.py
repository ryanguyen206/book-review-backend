from rest_framework import serializers
from .models import BookReview, Genre, Message



        
class BookReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='creator.username', read_only=True)
    genre_name = serializers.CharField(source='genre.genre', read_only=True)
    participants_count = serializers.SerializerMethodField()

    class Meta:
        model = BookReview
        fields = [
            'id',
            'creator',
            'genre',
            'genre_name',
            'username',
            'book_title',
            'review_title',
            'participants_count',
            'body',
            'created'
        ]
        read_only = ['participants_count',]
       
    def get_participants_count(self, obj):
        return obj.participants.count()
        
        
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre', 'id', 'pk']
        
        
class MessageSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Message
        fields = ['id', 'body', 'username', 'user', 'book_review', 'created']
        
 
