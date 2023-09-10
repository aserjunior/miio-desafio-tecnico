from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Movies(models.Model):
    id = models.PositiveIntegerField(primary_key=True, validators=[MinValueValidator(1)])
    adult = models.BooleanField()
    title = models.CharField(max_length=200)
    overview = models.TextField()
    release_date = models.CharField(max_length=12)
    vote_average =  models.DecimalField(max_digits=3, decimal_places=1,
                                        validators=[MinValueValidator(0)])
    popularity = models.DecimalField(max_digits=10,decimal_places=3,
                                     validators=[MinValueValidator(0)])
    
    def __str__(self):
        return self.title
    
    class Meta:
            db_table = 'Movies'