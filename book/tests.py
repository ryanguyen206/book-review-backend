from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from .models import BookReview, Genre
from .serializer import BookReviewSerializer
from django.contrib.auth.models import User

class BookReviewListOrCreateViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('book_review-list')
        self.user = User.objects.create_user(
        email='asdf@gmail.com',
        password='hiwa_asdf',
        username='smile as we go ahead'
    )
        self.client.force_authenticate(self.user)


    def test_get_book_reviews(self):

        genre = Genre.objects.create(genre='Fiction')
        BookReview.objects.create(book_title='Book 1', review_title='Good book', body='alright', genre=genre)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(BookReview.objects.count(), 1)


    def test_create_book_review(self):
        genre = Genre.objects.create(genre='Non-Fiction')
        data = {'book_title' : 'testing', 'review_title':'if i can', 'body':'create a book', 'genre':genre.pk}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(BookReview.objects.filter(book_title='testing').exists())
        
        
class BookReviewUpdateViewTest(APITestCase):
    def setUp(self) -> None:
  
        self.user = User.objects.create_user(
        email='asdf@gmail.com',
        password='hiwa_asdf',
        username='smile as we go ahead'
    )
        self.book_review = BookReview.objects.create(
            creator=self.user,
            book_title='Booky',
            review_title='Goody',
            body='Greaty',
            genre=Genre.objects.create(genre='Fiction')
        )
        self.url = reverse('book_review-update', kwargs={'pk': self.book_review.pk})
        self.client.force_authenticate(self.user)

    def test_update(self):
        updated_data = {
            'book_title': 'Updated Book 1',
            'review_title': 'Excellent book',
            'body': 'An outstanding read',
            'genre': Genre.objects.create(genre='Non-Fiction').pk
        }
        response = self.client.patch(self.url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_book_review = BookReview.objects.get(pk=self.book_review.pk)
        self.assertEqual(updated_book_review.book_title, updated_data['book_title'])
        self.assertEqual(updated_book_review.review_title, updated_data['review_title'])
        self.assertEqual(updated_book_review.body, updated_data['body'])
        self.assertEqual(updated_book_review.genre.genre, 'Non-Fiction')
        
class BookReviewDeleteViewTest(APITestCase):
    def setUp(self) -> None:
  
        self.user = User.objects.create_user(
        email='asdf@gmail.com',
        password='hiwa_asdf',
        username='smile as we go ahead'
    )
        self.book_review = BookReview.objects.create(
            creator=self.user,
            book_title='Delete Me',
            review_title='Delete!',
            body='Deletion',
            genre=Genre.objects.create(genre='Fiction')
        )
        self.url = reverse('book_review-destroy', kwargs={'pk': self.book_review.pk})
        self.client.force_authenticate(self.user)

    def test_delete_book_review(self):
       
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
class GenreListAPIView(APITestCase):
    def setUp(self):
        self.genre = Genre.objects.create(genre = 'Religion')
        self.genre = Genre.objects.create(genre = 'Magic')
        self.url = reverse('genre')
    
    def test_get_genres(self):
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Genre.objects.count(), 2)
        self.assertTrue(Genre.objects.filter(genre='Religion').exists())

        
        
    
   
        
        
        

