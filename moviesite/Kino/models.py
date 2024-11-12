from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField


class Profile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)], null=True, blank=True)
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    STATUS_CHOICES = (
        ('pro', 'pro'),
        ('simple', 'simple')
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='simple', null=True)

    def __str__(self):
        return self.status


class Country(models.Model):
    country_name = models.CharField(max_length=130, null=True, blank=True)

    def __str__(self):
        return f' {self.country_name}'


class Director(models.Model):
    director_name = models.CharField(max_length=32)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField(default=0)
    director_image = models.ImageField(upload_to='director_image/')

    def __str__(self):
        return f' {self.director_name}'


class Actor(models.Model):
    actor_name = models.CharField(max_length=32)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField(default=0)
    actor_image = models.ImageField(upload_to='actor_image', null=True, blank=True)

    def __str__(self):
        return f' {self.actor_name}'


class Janre(models.Model):
    janre_name = models.CharField(max_length=50)

    def __str__(self):
        return f' {self.janre_name}'


class Movie(models.Model):
    movie_name = models.CharField(max_length=40)
    year = models.DateField(auto_now=True)
    country = models.ManyToManyField(Country, related_name='country_movie')
    director = models.ManyToManyField(Director, related_name='director_movie')
    actor = models.ManyToManyField(Actor, related_name='actor_movie')
    janre = models.ManyToManyField(Janre, related_name='janre_movie')
    TYPES_CHOICES = (
        ('144', '144'),
        ('360', '360'),
        ('480', '480'),
        ('720', '720'),
        ('1080', '1080')
    )
    types = MultiSelectField(max_length=10, choices=TYPES_CHOICES, max_choices=5)
    movie_time = models.TimeField(auto_now=True)
    description = models.TextField()
    movie_trailer = models.FileField(verbose_name='видео', null=True, blank=True)
    movie_image = models.ImageField(upload_to='movie_image/', null=True, blank=True)
    Movie_STATUS = (
        ('pro', 'pro'),
        ('simple', 'simple')
    )
    status_movie = models.CharField(max_length=50, choices=Movie_STATUS, default='Pro')
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f' {self.movie_name}'

    def get_average_rating(self):
        ratings = self.rating.all()
        if ratings.exists():
            return round(sum(rating.stars for rating in ratings) / ratings.count(), 1)
        return 0


class MovieLanguages(models.Model):
    language = models.CharField(max_length=30)
    video = models.FileField(upload_to='movie_video')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.language}, {self.movie}'


class Moments(models.Model):
    movie = models.FileField(max_length=32)
    movie_moments = models.ForeignKey(Movie, related_name='moments', on_delete=models.CASCADE)


class Rating(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ManyToManyField(Movie, related_name='rating')
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)], verbose_name="Рейтинг", null=True, blank=True)
    parent = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.user}, {self.movie}'


class Favorite(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.user}'


class FavoriteMovie(models.Model):
    cart = models.ForeignKey(Favorite, on_delete=models.CASCADE, related_name='cart')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.cart}'


class History(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.user}, {self.movie}'
