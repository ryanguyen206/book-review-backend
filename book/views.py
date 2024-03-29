from django.shortcuts import render
from rest_framework import generics
from .models import BookReview, Genre, Message
from .serializer import BookReviewSerializer, GenreSerializer, MessageSerializer
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework import status
from .permissions import IsReviewCreatorOrReadOnly

#Book
class OneBookReviewAPIView(generics.RetrieveAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        
        if request.query_params.get('source') == 'review':
            instance.view_count += 1
            instance.save()
        response = super().get(request, *args, **kwargs)
        return response
        
class GetUserBookReviews(generics.ListAPIView):
    serializer_class = BookReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        user_id = self.kwargs['pk']
        queryset = BookReview.objects.filter(creator_id = user_id) 
        return queryset
    
class BookReviewListOrCreateView(generics.ListCreateAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
class BookReviewUpdateView(generics.UpdateAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer
    permission_classes = [IsReviewCreatorOrReadOnly]
     
class BookReviewDestroyView(generics.DestroyAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer
    permission_classes = [IsReviewCreatorOrReadOnly]

     
# Genre
class GenreListAPIView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        genre_names = [item['genre'] for item in data]

        return Response(genre_names)
    
# Message

class MessageListOrCreateAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        book_review_id = self.kwargs['pk']
        queryset = Message.objects.filter(book_review_id=book_review_id)    
        return queryset
    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
class GetRecentMessagesAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        user_id = self.kwargs['pk']
        queryset = Message.objects.filter(book_review__creator=user_id)
        return queryset


# User 

class UserCountView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        user_count = User.objects.count()
        data = {
            'user_count':user_count
        }
        
        return Response(data, status=status.HTTP_200_OK)
    
