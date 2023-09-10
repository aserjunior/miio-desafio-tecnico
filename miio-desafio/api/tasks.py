
import os
import requests
from celery import shared_task
from rest_framework import status
from .serializers import MovieSerializer


#Task to consume and save popular movies from TMDb API
@shared_task(bind=True)
def fetch_api_popular_movies(self):

    
    api_url = "https://api.themoviedb.org/3/movie/popular"
    api_key = os.environ.get('TMDB_API_KEY')
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == status.HTTP_200_OK:
        data = response.json()
        results = data.get('results', [])

        for movie_data in results:
            serializer = MovieSerializer(data=movie_data)
            if serializer.is_valid():
                serializer.save()

        return status.HTTP_200_OK
    else:
        return status.HTTP_500_INTERNAL_SERVER_ERROR

@shared_task(bind=True)    
def get_api_popular_movies(self):
    fetch_api_popular_movies.delay()