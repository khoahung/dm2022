import json

data_file = open("yelp/yelp_academic_dataset_review.json")
data = []
stop_line = 0
for line in data_file:
    if stop_line == 15:
        break
    else:
        data.append(json.loads(line)['text'])
        stop_line += 1
data_file.close()

len_dataset = list(map(len, data))


def init_clusters(reviews):
    clusters = []
    for i in reviews:
        clusters.append([len(i)])

    return clusters


clusters = init_clusters(data)

print(clusters)
