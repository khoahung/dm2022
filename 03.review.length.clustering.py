import json
import string
with open('./yelp/yelp_academic_dataset_review.json', encoding='utf8') as f:
    data = ""
    for line in f:
        data = line.strip()
        break
    dataJSON = json.loads(data)
    dataText = dataJSON['text']
    print(dataText)