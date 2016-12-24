import Phase1_genre as Genre
import Phase1_mood as Mood
import Phase1_theme as Theme
import get_data_from_es as get_data
import json_csv as convert_to_csv
import prediction_incomplete_data as predict
import push_completed_data_es as export_to_es

print('Getting movies which have complete data')
get_data.get_complete_data()
print('Getting movies which have incomplete data')
get_data.get_incomplete_data()
print('Convert movie details to csv')
convert_to_csv.convert()
print('Running mood classifier')
Mood.mood_main()
print('Running theme classifier')
Theme.theme_main()
print('Running genre classifier')
Genre.genre_main()
print('Predicting moods, themes, genre and keywords for incomplete data')
predict.prediction_for_incomplete_data()
print('Exporting completed data to es')
export_to_es.upload_to_es()
print('Done')
