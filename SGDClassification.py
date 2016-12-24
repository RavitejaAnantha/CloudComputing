def train(trainX, trainY):
    from sklearn.feature_extraction.text import CountVectorizer
    count_vect = CountVectorizer(analyzer='word', ngram_range=(1, 5), stop_words='english')
    X_train_counts = count_vect.fit_transform(trainX)
    from sklearn.feature_extraction.text import TfidfTransformer
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
    # from sklearn.naive_bayes import MultinomialNB
    # clf = MultinomialNB(alpha=2).fit(X_train_tfidf, trainY)
    from sklearn.linear_model import SGDClassifier
    clf = SGDClassifier(loss='modified_huber', penalty='l2', alpha=1e-3, n_iter=5, random_state=42).fit(X_train_tfidf,
                                                                                                        trainY)
    return clf, count_vect, tfidf_transformer


def test(docs_new, clf, count_vect, tfidf_transformer):
    X_new_counts = count_vect.transform(docs_new)
    X_new_tf = tfidf_transformer.transform(X_new_counts)

    predicted = clf.predict_proba(X_new_tf)
    predict_list = predicted.tolist()
    predict_dict = {}
    for i in range(0, len(clf.classes_)):
        predict_dict[clf.classes_[i]] = predict_list[0][i]
    sorted_predict_dict = sorted(predict_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_predict_dict
