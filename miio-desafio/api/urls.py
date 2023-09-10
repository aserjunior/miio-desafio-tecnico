from django.urls import path
from .views import MoviesListAndCreate, MoviesDetail, MoviesUpdate

urlpatterns = [
    #URLS TO VIEWS
    path('', MoviesListAndCreate.as_view(), name='list-create'),
    path('<int:id>/', MoviesDetail.as_view(), name='detail'),
    path('update/<int:id>/', MoviesUpdate.as_view(), name='update'),
]