import json

import requests


def upload_to_es():
    with open('complete_data.json', 'r') as f:
        lines = f.readlines()
        for line in lines:
            data_movie = json.loads(line)
            final_movie = json.dumps(data_movie)
            requests.post(
                'http://search-movies-5zcbuwmhuftqplir3dnm72jd4a.us-east-1.es.amazonaws.com/complete_movies/movie/',
                data=final_movie)
