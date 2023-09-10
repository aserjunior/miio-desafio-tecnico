from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from .factories import MoviesFactory, InvalidMoviesFactory
from mainapp.models import Movies

class MoviesAPITestCase(APITestCase):
    #setUp to facilitate use in tests
    def setUp(self):
        self.client = APIClient()

    #Test creating an movie with valid data
    def test_create_movies(self):

        url = reverse('list-create')

        movie_test = MoviesFactory.build()

        movie_request_json = {
            'id': movie_test.id,
            'adult': movie_test.adult,
            'title': movie_test.title,
            'overview': movie_test.overview,
            'release_date': movie_test.release_date,
            'vote_average': str(movie_test.vote_average),
            'popularity': str(movie_test.popularity),
        }

        response = self.client.post(url, movie_request_json, format='json')
    
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['id'], movie_request_json['id'])
        self.assertEqual(Movies.objects.count(), 1)
    
    #Test creating an movie with invalid data
    def test_invalid_create_movies(self):
        
        url = reverse('list-create')

        movie_test = InvalidMoviesFactory.build()

        movie_request_json = {
            'id': movie_test.id,
            'adult': movie_test.adult,
            'title': movie_test.title,
            'overview': movie_test.overview,
            'release_date': movie_test.release_date,
            'vote_average': str(movie_test.vote_average),
            'popularity': str(movie_test.popularity),
        }

        response = self.client.post(url, movie_request_json, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(Movies.objects.count(), 0)

    #Test getting specific details of an movie via id
    def test_get_movie_with_id(self):
        
        url_post = reverse('list-create')

        movie_test = MoviesFactory.build()

        movie_request_json = {
            'id': movie_test.id,
            'adult': movie_test.adult,
            'title': movie_test.title,
            'overview': movie_test.overview,
            'release_date': movie_test.release_date,
            'vote_average': str(movie_test.vote_average),
            'popularity': str(movie_test.popularity),
        }

        response_post = self.client.post(url_post, movie_request_json, format='json')
        
        url = reverse('detail', args=[movie_request_json['id']])  
        
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)  

        self.assertEqual(response.data['id'], movie_test.id)
        self.assertEqual(response.data['title'], movie_test.title)

    #Test getting specific details of an movie with invalid id
    def test_get_movie_with_invalid_id(self):
        
        url_post = reverse('list-create')
        #Using .build() because .create() wasn't working right
        movie_test = InvalidMoviesFactory.build()

        movie_request_json = {
            'id': movie_test.id,
            'adult': movie_test.adult,
            'title': movie_test.title,
            'overview': movie_test.overview,
            'release_date': movie_test.release_date,
            'vote_average': str(movie_test.vote_average),
            'popularity': str(movie_test.popularity),
        }

        response_post = self.client.post(url_post, movie_request_json, format='json')
        
        url = reverse('detail', args=[movie_request_json['id']])
        
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)