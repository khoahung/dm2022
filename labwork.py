import json
import string
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


with open('./yelp/yelp_academic_dataset_review.json', encoding='utf8') as f:
    data = ""
    for line in f:
        data = line.strip()
        break
    dataJSON = json.loads(data)

    dataText = dataJSON['text']
    dataText = dataText.translate(str.maketrans('', '', string.punctuation))
    print('remove punctuation===>',dataText)
    noBreakLine = dataText.replace('\n', ' ').replace('\r', '')
    print('remove Break Line===>',noBreakLine)
    arrayWord = noBreakLine.split(" ")
    print('Count occurence:',len(arrayWord))

    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(noBreakLine)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    print(word_tokens)
    print('String remove stop word=====>',' '.join(filtered_sentence))