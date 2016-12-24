import pandas as pd
from sklearn.externals import joblib

import SGDClassification as classifier
import pickle_object as pickler


def genre_main():
    df = pd.read_csv('genres.csv', header=0, sep='\s+')
    df = df[df.genres.notnull()]
    trainX_genre = df.iloc[:, 0].values
    trainY_genre = df.iloc[:, 1].values
    genre, count_vect_genre, tfidf_transformer_genre = classifier.train(trainX_genre, trainY_genre)
    object = pickler.PickleObjectWrapper()
    object.param1 = genre
    object.param2 = count_vect_genre
    object.param3 = tfidf_transformer_genre
    filename = 'genre_model.sav'
    joblib.dump(object, filename)
    del object
    del genre
    del count_vect_genre
    del tfidf_transformer_genre
