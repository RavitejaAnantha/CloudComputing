import requests
import json
def get_complete_data():
    query = json.dumps({"query": {
                "exists": {
                    "field": "video_urls"

        }
    }})

    res = requests.get(
        'http://search-movies-5zcbuwmhuftqplir3dnm72jd4a.us-east-1.es.amazonaws.com/complete_movies/_search?size=10000',data=query).json()
    for hit in res['hits']['hits']:
        with open('data.json', 'a') as f:

            f.write(json.dumps(hit["_source"]))
            f.write('\n')

get_complete_data()