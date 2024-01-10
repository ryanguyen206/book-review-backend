from django.urls import path
from . import views

urlpatterns = [
    path('book-review/', views.BookReviewListOrCreateView.as_view(), name='book_review-list'),
    path('book-review/<int:pk>/', views.OneBookReviewAPIView.as_view(), name='book_review-detail'),
    path('book-review/<int:pk>/update/', views.BookReviewUpdateView.as_view(), name='book_review-update'),
    path('book-review/<int:pk>/delete/', views.BookReviewDestroyView.as_view(), name='book_review-destroy'),
    
    path('genre/', views.GenreListAPIView.as_view(), name='genre'),
    
    path('book-review/<int:pk>/messages/', views.MessageListOrCreateAPIView.as_view(), name='message-list'),
 

]