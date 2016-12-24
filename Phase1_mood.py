import pandas as pd
from sklearn.externals import joblib

import SGDClassification as classifier
import pickle_object as pickler


def mood_main():
    df = pd.read_csv('moods.csv', header=0, sep='\s+')
    trainX_mood = df.iloc[:, 0].values
    trainY_mood = df.iloc[:, 1].values

    mood, count_vect_mood, tfidf_transformer_mood = classifier.train(trainX_mood, trainY_mood)
    object = pickler.PickleObjectWrapper()
    object.param1 = mood
    object.param2 = count_vect_mood
    object.param3 = tfidf_transformer_mood
    filename = 'mood_model.sav'
    joblib.dump(object, filename)
    del object
    del mood
    del count_vect_mood
    del tfidf_transformer_mood
