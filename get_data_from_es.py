import json

import requests


def get_complete_data():
    res = requests.get(
        'http://search-movies-5zcbuwmhuftqplir3dnm72jd4a.us-east-1.es.amazonaws.com/complete_movies/_search?size=10000').json()
    for hit in res['hits']['hits']:
        with open('data.json', 'a') as f:
            f.write(json.dumps(hit["_source"]))
            f.write('\n')


def get_incomplete_data():
    res = requests.get(
        'http://search-movies-5zcbuwmhuftqplir3dnm72jd4a.us-east-1.es.amazonaws.com/incomplete_movies/_search?size=10000').json()
    for hit in res['hits']['hits']:
        with open('incomplete_data.json', 'a') as f:
            f.write(json.dumps(hit["_source"]))
            f.write('\n')
