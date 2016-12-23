import json
import requests
from Naked.toolshed.shell import execute_js
import os
from Image_feature_extraction_code import get_image_features
import glob
from Get_movies_es import get_complete_data

def get_video(filename,s3_url):
    r = requests.get(s3_url, stream=True)
    with open(filename+'.mp4', 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)


get_complete_data()

with open('data.json', 'r') as f:
    lines = f.readlines()
    for line in lines:
        data = json.loads(line)
        if 'video_urls' in data:
            key=data['key']
            video_urls = data['video_urls']
            if 's3_url' in video_urls:
                s3_url=data['video_urls']['s3_url']

                #get_video(key,s3_url)
                success = execute_js('video2img.js',s3_url+' '+key)
                if success:
                    path = './output/'
                    dict_movie={'movie_key':key}
                    image_features=[]
                    for image_name in os.listdir(path):
                        if image_name == '.DS_Store':
                            continue
                        if key in image_name:
                            feature_dict=get_image_features(os.path.join(path,image_name))
                            dict_features={'filename':image_name,'features':feature_dict}
                            image_features.append(dict_features)

                    '''To delete all images in the folder uncomment the below code'''
                    # files = glob.glob(os.path.join(path,'*'))
                    # for f2 in files:
                    #     os.remove(f2)
                    dict_movie['features']=image_features
                    with open('movie_features.json', 'a') as f1:
                        f1.write(json.dumps(dict_movie))
                        f1.write('\n')
                        #os.remove(key+'.mp4') Delete video in the end
                else:
                    print('something went wrong while running splitting video to images')
