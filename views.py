from django.shortcuts import render
from .models import Film, Cinema, FilmScreening


def index_page(request):
    project_name = "Cinema LAB 8"
    student_info = {
        'full_name': 'Малюшицький Богдан Петрович',
        'group': 'КН-22004бск',
        'italic_style': 'italic',  # Стиль курсивом
        'color_style': 'color: blue;',  # Стиль кольором
    }

    films = Film.objects.all()
    cinemas = Cinema.objects.all()
    screenings = FilmScreening.objects.all()

    return render(request, 'index.html', {
        'project_name': project_name,
        'student_info': student_info,
        'films': films,
        'cinemas': cinemas,
        'screenings': screenings,
    })