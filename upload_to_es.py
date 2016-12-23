import json
import requests
def upload_to_es():
    with open('scene_details.json.json', 'r') as f:
        lines = f.readlines()
        for line in lines:
            data_scene = json.loads(line)
            final_scene = json.dumps(data_scene)
            requests.post('<url of es with index and topic>',
                data=final_scene)