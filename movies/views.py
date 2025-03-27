from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm

def index(request):
    movies = Movie.objects.all()  # Fetch movies from the database
    return render(request, 'movies/index.html', {'movies': movies})

def about(request):
    return render(request, 'movies/about.html')

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MovieForm()
    return render(request, 'movies/add_movie.html', {'form': form})

def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/edit_movie.html', {'form': form})

def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('index')
    return render(request, 'movies/delete_movie.html', {'movie': movie})