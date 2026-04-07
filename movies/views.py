from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Genre, Favourite
from django.contrib.auth.decorators import login_required

def movie_list(request):
    query = request.GET.get('q')
    movies = Movie.objects.all()
    if query:
        movies = movies.filter(title__icontains=query)
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

@login_required
def add_favourite(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    Favourite.objects.get_or_create(user=request.user, movie=movie)
    return redirect('movie_detail', pk=pk)
