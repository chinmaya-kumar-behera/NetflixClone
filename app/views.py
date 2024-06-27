from django.shortcuts import render,HttpResponse
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


def getMovieDataById(request, id):    
    movie_url = f'https://api.themoviedb.org/3/movie/{id}?api_key={API_KEY}&language=en-US'
    video_url = f'https://api.themoviedb.org/3/movie/{id}/videos?api_key={API_KEY}&language=en-US'
    credits_url = f'https://api.themoviedb.org/3/movie/{id}/credits?api_key={API_KEY}&language=en-US'
    recommendations_url = f'https://api.themoviedb.org/3/movie/{id}/recommendations?api_key={API_KEY}&language=en-US'
    
    movie_response = requests.get(movie_url)
    video_response = requests.get(video_url)
    credits_response = requests.get(credits_url)
    recommendations_response = requests.get(recommendations_url)
    
    if all(response.status_code == 200 for response in [movie_response, video_response, credits_response, recommendations_response]):
        movie_data = movie_response.json()
        video_data = video_response.json()
        credits_data = credits_response.json()
        recommendations_data = recommendations_response.json()
        video_key = None
        
        # Find the trailer video key
        for video in video_data.get('results', []):
            if video['type'] == 'Trailer' and video['site'] == 'YouTube':
                video_key = video['key']
                break
        
        # Get the list of starring actors (up to 5)
        cast = credits_data.get('cast', [])[:5]
        recommendations = recommendations_data.get('results', [])[:12]
        
        context = {
            'movie': movie_data,
            'video_key': video_key,
            'cast': cast,
            'recommendations': recommendations,
        }

        return render(request, 'movie_details.html', context)
    else:
        return HttpResponse("Movie not found")