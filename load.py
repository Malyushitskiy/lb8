from django.core.management.base import BaseCommand
from myapp.models import Film, Cinema, FilmScreening
from datetime import date
import random

class Command(BaseCommand):
    help = 'Populate Film, Cinema, and FilmScreening tables with data'

    def handle(self, *args, **options):
        # Додаємо фільми (11 фільмів)
        films_data = [
            {
                'title': 'Фільм 1',
                'genre': 'мелодрама',
                'duration': 120,
                'rating': 8.5,
            },
            {
                'title': 'Фільм 2',
                'genre': 'комедія',
                'duration': 90,
                'rating': 7.8,
            },
            {
                'title': 'Фільм 3',
                'genre': 'бойовик',
                'duration': 110,
                'rating': 9.0,
            },
            {
                'title': 'Фільм 4',
                'genre': 'мелодрама',
                'duration': 95,
                'rating': 7.2,
            },
            {
                'title': 'Фільм 5',
                'genre': 'комедія',
                'duration': 100,
                'rating': 8.1,
            },
            {
                'title': 'Фільм 6',
                'genre': 'бойовик',
                'duration': 130,
                'rating': 9.5,
            },
            {
                'title': 'Фільм 7',
                'genre': 'мелодрама',
                'duration': 85,
                'rating': 7.5,
            },
            {
                'title': 'Фільм 8',
                'genre': 'комедія',
                'duration': 110,
                'rating': 8.7,
            },
            {
                'title': 'Фільм 9',
                'genre': 'бойовик',
                'duration': 125,
                'rating': 9.2,
            },
            {
                'title': 'Фільм 10',
                'genre': 'мелодрама',
                'duration': 95,
                'rating': 7.0,
            },
            {
                'title': 'Фільм 11',
                'genre': 'комедія',
                'duration': 105,
                'rating': 8.3,
            },
        ]

        for data in films_data:
            film = Film(**data)
            film.save()

        # Додаємо кінотеатри (3 кінотеатри)
        cinemas_data = [
            {
                'name': 'Кінотеатр 1',
                'ticket_prices': 10.0,
                'seats_count': 100,
                'address': 'Адреса 1',
                'phone': '123-456-7890',
            },
            {
                'name': 'Кінотеатр 2',
                'ticket_prices': 12.0,
                'seats_count': 120,
                'address': 'Адреса 2',
                'phone': '987-654-3210',
            },
            {
                'name': 'Кінотеатр 3',
                'ticket_prices': 15.0,
                'seats_count': 150,
                'address': 'Адреса 3',
                'phone': '555-555-5555',
            },
            # Додайте дані для інших кінотеатрів
        ]

        for data in cinemas_data:
            cinema = Cinema(**data)
            cinema.save()

        screenings_data = []

        for _ in range(15):
            data = {
                'film': Film.objects.order_by('?').first(),
                'cinema': Cinema.objects.order_by('?').first(),
                'start_date': date(2023, random.randint(1, 12), random.randint(1, 28)),
                'show_duration': random.randint(1, 5),
            }
            screenings_data.append(data)

        for data in screenings_data:
            screening = FilmScreening(**data)
            screening.save()

        self.stdout.write(self.style.SUCCESS('Successfully filled Film, Cinema, and FilmScreening tables'))
