import json
import csv

print('Start\n')
count = 0
parsed_json = []

# should be put before updating
with open('image_features.csv', 'a') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC, delimiter=' ')
    writer.writerow(('movie_name', 'image_name', 'watson_object_1', 'watson_object_2', 'watson_object_3', 'watson_face',
                     'microsoft_emotion_1', 'microsoft_emotion_2', 'microsoft_emotion_3', 'genre'))

movie_name = ''
image_name = ''
watson_object_1 = ''
watson_object_2 = ''
watson_object_3 = ''
watsonFace = 0
microsoft_emotion_1 = ''
microsoft_emotion_2 = ''
microsoft_emotion_3 = ''
genre = ''


def initialize():
    movie_name = ''
    image_name = ''
    watson_object_1 = ''
    watson_object_2 = ''
    watson_object_3 = ''
    watsonFace = 0
    microsoft_emotion_1 = ''
    microsoft_emotion_2 = ''
    microsoft_emotion_3 = ''
    genre = ''


# scene_data = open('res.csv', 'w')
# csvwriter = csv.writer(scene_data)

with open('data.json','r') as f:
    lines = f.readlines()
    for line in lines:
        parsed_json = json.loads(line)

        print(parsed_json)

        movie_name = parsed_json['movie_key']
        features = parsed_json['features']
        for thumb in features:
            image_name = thumb['filename']
            model_used = thumb['features']

            if 'watsonFace' in model_used:
                if model_used['watsonFace']:
                    watsonFace = 1

            if 'watsonClassify' in model_used:
                classes = model_used['watsonClassify']['images'][0]["classifiers"][0]["classes"]
                # print type(classes)
                sorted_classes = sorted(classes, key=lambda k: k['score'], reverse=True)
                # print sorted_classes
                # print 'Sorted Clases'
                list_watson_objects = []
                # count = 0
                # if len(sorted_classes)>=3:
                # 	watson_object_1 = myclass['class']
                # 	for myclass in sorted_classes:
                for i in range(len(sorted_classes)):
                    if (i < 3):
                        myclass = sorted_classes[i]
                        list_watson_objects.append(myclass['class'])
                    # print myclass['class']

                if len(list_watson_objects) == 3:
                    watson_object_1 = list_watson_objects[0]
                    watson_object_2 = list_watson_objects[1]
                    watson_object_3 = list_watson_objects[2]

                if len(list_watson_objects) == 2:
                    watson_object_1 = list_watson_objects[0]
                    watson_object_2 = list_watson_objects[1]
                # watson_object_3 already = ''

                if len(list_watson_objects) == 1:
                    watson_object_1 = list_watson_objects[0]

            if 'microsoftEmotion' in model_used:
                classes = model_used['microsoftEmotion']
                if len(classes) != 0:
                    scores = {}
                    list_score_objects = []
                    # print classes
                    # print len(classes)
                    # print type(classes)
                    for myclass in classes:
                        scores = myclass['scores']

                    sorted_scores = sorted(scores.items(), key=lambda k: k[1], reverse=True)

                    for i in range(len(sorted_scores)):
                        if (i < 3):
                            list_score_objects.append(sorted_scores[i][0])
                        # print sorted_scores[i][0]

                    if len(list_score_objects) == 3:
                        microsoft_emotion_1 = list_score_objects[0]
                        microsoft_emotion_2 = list_score_objects[1]
                        microsoft_emotion_3 = list_score_objects[2]

                    if len(list_score_objects) == 2:
                        microsoft_emotion_1 = list_score_objects[0]
                        microsoft_emotion_2 = list_score_objects[1]

                    if len(list_score_objects) == 1:
                        microsoft_emotion_1 = list_score_objects[0]
            with open('image_features.csv', 'a') as csvfile:
                writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC, delimiter=' ')
                writer.writerow((movie_name, image_name, watson_object_1, watson_object_2, watson_object_3, watsonFace,
                                 microsoft_emotion_1, microsoft_emotion_2, microsoft_emotion_3))
            initialize()
