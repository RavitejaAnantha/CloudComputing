import pandas as pd
from sklearn.externals import joblib

import SGDClassification as classifier
import pickle_object as pickler


def theme_main():
    df = pd.read_csv('themes.csv', header=0, sep='\s+')
    trainX_theme = df.iloc[:, 0].values
    trainY_theme = df.iloc[:, 1].values

    theme, count_vect_theme, tfidf_transformer_theme = classifier.train(trainX_theme, trainY_theme)
    object = pickler.PickleObjectWrapper()
    object.param1 = theme
    object.param2 = count_vect_theme
    object.param3 = tfidf_transformer_theme
    filename = 'theme_model.sav'
    joblib.dump(object, filename)
    del theme
    del count_vect_theme
    del tfidf_transformer_theme
    del object
