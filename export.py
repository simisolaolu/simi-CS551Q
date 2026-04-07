import os
import django
import pandas as pd
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_explorer.settings')
django.setup()

from movies.models import Movie, Genre

data = pd.read_csv('movies_small.csv')

for _, row in data.iterrows():
    title = row['title']
    match = re.search(r'\((\d{4})\)$', title)
    release_year = int(match.group(1)) if match else None
    clean_title = re.sub(r'\(\d{4}\)$', '', title).strip()
    genre_name = row['genres'].split('|')[0]
    genre, _ = Genre.objects.get_or_create(name=genre_name)

    Movie.objects.create(
        title=clean_title,
        release_year=release_year,
        rating=0.0,
        description="Sample description",
        genre=genre
    )