import json

with open('data.json', 'r') as f:
    lines=f.readlines()
    movie_key=set()
    for line in lines:
        data=json.loads(line)
        if 'video_urls' in data and 's3_url' in data['video_urls'] and 'picture_url' in data and data['picture_url']!='' and data['picture_url']!='N/A' and len(data['actors'])!=0 and len(data['directors'])!=0:
            if data['key'] not in movie_key:
                movie_key.add(data['key'])
                with open('data_final.json', 'a') as f1:
                    f1.write(json.dumps(data))
                    f1.write('\n')