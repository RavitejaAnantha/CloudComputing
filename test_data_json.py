from sklearn.externals import joblib

import SGDClassification as classifier

model = joblib.load('genre_model.sav')

dict_test_movie = {
    "title": "The Other Side of Heaven",
    "actors": [

    ],
    "directors": [

    ],
    "genres": [

    ],
    "release_year": "2002",
    "key": "theothersideofheaven-2002",
    "synopsis": "A young man from Idaho finds himself in a beautiful but dangerous land in the South Pacific as he follows his faith and tries to spread it to others in this adventure-drama, based on a true story. In 1953, John Groberg (Christopher Gorham) is a 19-year-old student at Brigham Young University, whose greatest adventure in life had been to leave home to go to school in Utah. That all changes when Groberg accepts a missionary assignment in the Tonga Islands near Fiji; Groberg is instructed to \"build a kingdom\" and educate the natives about the Mormon faith, even though he knows little of their customs and nothing of their language. Leaving behind his sweetheart, Jean Sabin (Anne Hathaway), Groberg arrives in Tonga and is quickly immersed in the native culture, and strives to teach the Tongans about the teachings of the Latter-Day Saints while trying to respect their cultural traditions and face the joys and struggles of primitive life in the South Pacific alongside them. Groberg makes a valuable ally in Feki (Joe Folau), a Tongan who becomes an avid follower of the Mormon faith, but he also finds his loyalty to Jean (with whom he's been maintaining a long-distance relationship through cards and letters) tested when a native girl makes her attraction to him quite clear. Based on the real John Groberg's memoir In the Eye of the Storm, The Other Side of Heaven was produced by Jerry Molen, Academy Award winning producer of Schindler's List and Jurassic Park; it also marked the directorial debut of screenwriter Mitch Davis.",
    "keywords": [
        "correspondence",
        "culture-shock",
        "girlfriend",
        "hurricane",
        "island-tropical",
        "long-distance",
        "missionary",
        "native",
        "service",
        "shipwreck",
        "traveling"
    ],
    "themes": [
        "Fish Out of Water",
        "Missionaries"
    ],
    "moods": [
        "Triumph of the Spirit"
    ],
    "review": "This is an excellent adaptation of the memoirs of John Groberg, who, in the 1950s, served a mission to the Tongan Islands on behalf of his church. Actors Christopher Gorham and Anne Hathaway star as Groberg and his sweetheart, Jean Sabin, along with a strong cast of supporting actors. This family-friendly film follows Groberg as he leaves the comfort of his home in Idaho Falls, ID, to embark on his mission to a Southern Pacific country neither he nor his family has even heard of. He faces lengthy travel delays, unconventional connections, and even has to work his way across the sea to get to his destination. Once he arrives, he is faced by a suspicious group of natives who are a little too eager to enjoy his culture shock. Yet through nearly three years of service, Groberg learns to love the people he's been sent to serve. He maintains regular contact throughout his mission with his sweetheart, whose letters help sustain him in his moments of despair and provide the movie's sense of romance. There is no lack of adventure in this film as the islands were prone to severe weather. The special effects for the hurricane and shipwreck scenes are breathtaking."
}

genre = model.param1
count_vector_genre = model.param2
tfidf_transformer_genre = model.param3
docs_new = [dict_test_movie['synopsis']]
predictions = classifier.test(docs_new, genre, count_vector_genre, tfidf_transformer_genre)
genres = []
for i in range(0, len(predictions)):
    if len(genres) < 5:
        genres.append(predictions[i][0])
dict_test_movie['genres'] = genres
print(dict_test_movie)
