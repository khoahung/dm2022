import numpy as np
import math
from random import seed, randint
seed(1)

data = [randint(1, 150) for i in range(150)]
print(data)

num_centroids = 3
clusters = {k: {'points': [], 'center': randint(1, 150), 'movable': True} for k in range(num_centroids)}

print(clusters)

while True:
    for point in data:
        pointCenterList = []
        for index, cluster in clusters.items():
            dist = abs(cluster['center'] - point)
            pointCenterList.append((dist, index))
        _, index = min(pointCenterList, key=lambda x:x[0])
        clusters[index]['points'].append(point)

    for index, cluster in clusters.items():
        new_center = sum(cluster['points'])/len(cluster['points'])
        if abs(cluster['center'] - new_center) < 0.005:
             cluster['movable'] = False
        else:
            cluster['center'] = new_center
    print('===')
    print(clusters)
    print('===')

    if True in [cluster['movable'] for index, cluster in clusters.items()]:
        for index, cluster in clusters.items():
            cluster['points'] = []
    else:
        break
