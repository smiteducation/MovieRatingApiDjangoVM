from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

    def totalRatings(self):
        ratings = Ratings.objects.filter(movie=self)
        return(len(ratings))

    def averageRating(self):
        ratings = Ratings.objects.filter(movie=self)
        averagerating = 0
        totalstars = 0
        if len(ratings) > 0:
            for rating in ratings:
                totalstars += rating.stars
            averagerating = totalstars/len(ratings)

        return averagerating

class Ratings(models.Model):
    movie = models.ForeignKey(Movies,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(default=1, validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        unique_together = (('user','movie'),)
        index_together = (('user','movie'),)