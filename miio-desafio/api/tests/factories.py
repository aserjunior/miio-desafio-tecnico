from factory import Faker, Factory
from mainapp.models import Movies

#Factory with right data
class MoviesFactory(Factory):
    class Meta:
        model = Movies

    id = Faker('random_int', min=1, max=9999)
    adult = Faker('boolean')
    title = Faker('word')
    overview = Faker('text')
    release_date = Faker('date_between', start_date='-30y', end_date='today')
    vote_average = Faker('pydecimal', left_digits=1, right_digits=1, positive=True)
    popularity = Faker('pydecimal', left_digits=3, right_digits=3, positive=True)

#Factory with wrong data
class InvalidMoviesFactory(Factory):
    class Meta:
        model = Movies

    id = 0 #Invalid id
    adult = Faker('boolean')
    title = Faker('word')
    overview = Faker('text')
    release_date = Faker('date_between', start_date='-30y', end_date='today')
    vote_average = Faker('pydecimal', left_digits=1, right_digits=1, positive=False) #Negative Notes
    popularity = Faker('pydecimal', left_digits=3, right_digits=3, positive=False, max_value=1000.0)
