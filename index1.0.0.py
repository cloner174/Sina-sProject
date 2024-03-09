from pymnet import *
import matplotlib.pyplot as plt


g = MultilayerNetwork(aspects=1,
                      fullyInterconnected=False)


g.add_layer('adv')
g.add_layer('pub')


import json
with open('data/result.json', 'r') as file:
    data = json.load(file)


nodes = data['nodes']
edges = data['links']


Esource = []
for i in range(len(edges)):
    temp = edges[i]
    Esource.append(temp['source'])



Etarget = []
for i in range(len(edges)):
    temp = edges[i]
    Etarget.append(temp['target'])


edges = []
for i in range(5000):
    temp = (Esource[i], Etarget[i])
    edges.append(temp)



for edge in edges:
    sor = edge[0]
    tar = edge[1]
    g[sor, tar, 'adv','pub'] = 1



draw(g, layergap=2.5)


plt.title('Network of advertisers and publishers')



#plt.xlabel("X-axis Label")
#plt.ylabel("Y-axis Label")


plt.show()