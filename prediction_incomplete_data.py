import json

from sklearn.externals import joblib

import EntityExtract as KeyWord
import SGDClassification as classifier


def prediction_for_incomplete_data():
    mood_model = joblib.load('mood_model.sav')
    theme_model = joblib.load('theme_model.sav')
    genre_model = joblib.load('genre_model.sav')
    with open('incomplete_data.json', 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = json.loads(line)
            if (len(data['moods']) != 0 and len(data['themes']) != 0 and len(data['genres']) != 0 and len(
                    data['keywords']) != 0) or data['synopsis'] == '':
                with open('complete_data.json', 'a') as f1:
                    f1.write(json.dumps(data))
                    f1.write('\n')
            else:
                if len(data['moods']) == 0:
                    docs_new = [data['synopsis']]
                    predictions = classifier.test(docs_new, mood_model.param1
                                                  , mood_model.param2, mood_model.param3)
                    moods = []
                    for i in range(len(predictions)):
                        if len(moods) < 5:
                            moods.append(predictions[i][0])
                    data['moods'] = moods
                if len(data['themes']) == 0:
                    docs_new = [data['synopsis']]
                    predictions = classifier.test(docs_new, theme_model.param1
                                                  , theme_model.param2, theme_model.param3)
                    themes = []
                    for i in range(len(predictions)):
                        if len(themes) < 5:
                            themes.append(predictions[i][0])
                    data['themes'] = themes
                if len(data['genres']) == 0:
                    docs_new = [data['synopsis']]
                    predictions = classifier.test(docs_new, genre_model.param1
                                                  , genre_model.param2, genre_model.param3)
                    genres = []
                    for i in range(len(predictions)):
                        if len(genres) < 5:
                            genres.append(predictions[i][0])
                    data['genres'] = genres
                if len(data['keywords']) == 0:
                    keywords = KeyWord.entity_extract_main(data['synopsis'])
                    data['keywords'] = keywords
                with open('complete_data.json', 'a') as f1:
                    f1.write(json.dumps(data))
                    f1.write('\n')
