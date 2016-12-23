import csv
import copy
import json
input_file = csv.DictReader(open("image_features.csv"),delimiter=' ')
for row in input_file:
    features=copy.deepcopy(row)
    features.pop('image_name', None)
    features.pop('movie_name',None)
    genres=row['genres']
    from_timestamp=row['image_name'][-17:]
    from_timestamp=from_timestamp[from_timestamp.index('-')+1:]
    from_timestamp=int(from_timestamp[:from_timestamp.index('-')])
    to_timestamp=from_timestamp+5
    scene_order=from_timestamp/5
    key=row['movie_name']
    scene_dict={'key':key,'scene_order':scene_order,'features':features,'from_timestamp':from_timestamp,'to_timestamp':to_timestamp}
    with open('scene_details.json', 'a') as f:
        f.write(json.dumps(scene_dict))
        f.write('\n')

