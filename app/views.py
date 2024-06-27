# movies/views.py
from django.shortcuts import render
import requests

API_KEY = '230705515d651555c10a08900459b838'

def home(request):
    trending_url = f'https://api.themoviedb.org/3/trending/movie/week?api_key={API_KEY}'
    popular_url = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}'
    top_rated_url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}'
    upcoming_url = f'https://api.themoviedb.org/3/movie/upcoming?api_key={API_KEY}'

    trending_movies = requests.get(trending_url).json().get('results', [])
    popular_movies = requests.get(popular_url).json().get('results', [])
    top_rated_movies = requests.get(top_rated_url).json().get('results', [])
    upcoming_movies = requests.get(upcoming_url).json().get('results', [])

    context = {
        'trending_movies': trending_movies,
        'popular_movies': popular_movies,
        'top_rated_movies': top_rated_movies,
        'upcoming_movies': upcoming_movies,
    }
    return render(request, 'home.html', context)



def login(request):
    return render(request,'login.html')
