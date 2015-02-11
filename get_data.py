#!usr/bin/python

import requests
import json

# API key to be used in themoviedatabse
API_KEY = "25473a3c2aa41a9574691343fe496076"
SEARCH_URL = "https://api.themoviedb.org/3/search/movie"

# Getting response from bbc website and parsing the json data
bbc_response = requests.get("http://www.bbc.co.uk/tv/programmes/formats/films/player/episodes.json")
iplayer_movies = bbc_response.json()

# List to collect all movies listed in the database
ratings = []

for movie in iplayer_movies['episodes']:
    title = movie['programme']['display_titles']['title']
    image = movie['programme']['image']['pid']
    prog = movie['programme']['pid']

    params = {
                'api_key': API_KEY,
                'query'  : title
            }
    
    # Sending get request to TMD API 
    movie_search_response = requests.get(SEARCH_URL, params=params)

    # Checking for status_code off response
    if movie_search_response.status_code==200:

        movie_search_results = movie_search_response.json()

        # Exception handling in case jsondata is empty
        try:
            movie_rating = str(movie_search_results['results'][0]['vote_average'])
        except IndexError:
            movie_rating = "Movie not listed on TMD"
    else:
        movie_rating = "Not found"

    result =  {
                'title': title,
                'rating': movie_rating,
                'image': image,
                'prog': prog
                }

    # Appending results for each movie in single file
    ratings.append(result)
