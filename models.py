from django.db import models

# Модель "Фільми"
class Film(models.Model):
    film_code = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    genre_choices = [
        ('мелодрама', 'Мелодрама'),
        ('комедія', 'Комедія'),
        ('бойовик', 'Бойовик'),
    ]
    genre = models.CharField(max_length=15, choices=genre_choices)
    duration = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)

# Модель "Кінотеатри"
class Cinema(models.Model):
    cinema_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    ticket_prices = models.DecimalField(max_digits=8, decimal_places=2)
    seats_count = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

# Модель "Транслювання фільмів"
class FilmScreening(models.Model):
    screening_code = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    start_date = models.DateField()
    show_duration = models.PositiveIntegerField()
