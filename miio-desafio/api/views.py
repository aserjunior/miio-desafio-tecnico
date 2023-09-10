from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from mainapp.models import Movies
from .serializers import MovieSerializer
from .tasks import get_api_popular_movies

class MoviesListAndCreate(APIView):
    """
    API Endpoint - GET List 20 Popular Movies/POST an movie
    """

    #20 popular movies
    def get(self, request):
        query_movies = Movies.objects.all().order_by('-popularity')[:20]
        serializer = MovieSerializer(query_movies, many=True)
        return Response(serializer.data)

    #Create a new Movie
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MoviesDetail(APIView):
    """
    API Endpoint - GET especific movie
    """

    #Get an specific movie to see its details
    def get(self, request, id):
        #Checks if movie with the specif id exists
        try:
            specific_movie = Movies.objects.get(id=id)
            serializer = MovieSerializer(specific_movie)
            return Response(serializer.data)
        except Movies.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class MoviesUpdate(APIView):
    """
    API Endpoint - Update with partial/full data object
    """

    #Update specific fields, only need to provide fields you want to update
    def patch(self, request, id):
        #Checks if objects exists
        try:
            specific_movie = Movies.objects.get(id=id)
        except Movies.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        #If it exists, checks if data is valid
        serializer = MovieSerializer(specific_movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Update all the object, needs to be provider all fields 
    def put(self, request, id):
        #Checks if objects exists
        try:
            specific_movie = Movies.objects.get(id=id)
        except Movies.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        #If it exists, checks if data is valid
        serializer = MovieSerializer(specific_movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)