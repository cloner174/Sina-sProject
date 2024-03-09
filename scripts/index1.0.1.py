#
from pymnet import *
import matplotlib.pyplot as plt
import pandas as pd

g = MultilayerNetwork(aspects=1,
                      fullyInterconnected=False)

g.add_layer('adv')
g.add_layer('pub')
with open('data/interactions.csv', 'r') as file:
     data = pd.read_csv(file)

data.head()
#ID  Campaign Content - Content → Campaign ID  Campaign Campaign - Campaign → Advertiser ID  Media App Media - Media → Publisher ID
#0  2767759                                     37391                                         93786                                   71795
#1  2767754                                     37391                                         93786                                   48669
#2  2767741                                     37391                                         93786                                   15969
#3  2767885                                     37391                                         93786                                   42332
#4  2767747                                     37391                                         93786                                   93324


type(data)
#<class 'pandas.core.frame.DataFrame'>

#data.iloc[:, 1].unique()
#array([37391, 39035, 40616, ..., 42723, 42826, 42302])

nodes = list(data.iloc[:, 1].unique())
print(len(nodes))

a = list(data.iloc[:, 2].unique())
b = list(data.iloc[:, 3].unique())
print(len(a))
print(len(b))




#data.columns
#Index(['ID', 'Campaign Content - Content → Campaign ID',
#       'Campaign Campaign - Campaign → Advertiser ID',
#       'Media App Media - Media → Publisher ID'],
#      dtype='object')


A = dataINT.iloc[:,2]
B = dataINT.iloc[:,2]


a = list(dataINT.iloc[:,2].unique())
b = list(dataINT.iloc[:,3].unique())



nodez = []
for i in a:
   nodez.append(i)


for i in b:
    nodez.append(i)

print(len(nodez))

#data.shape
#(108813, 4)
#len(A)

#type(A)
#<class 'pandas.core.series.Series'>
A = list(A)
B = list(B)


edges = []
for i in range(20000):#        #            # Can be manually set
    temp = (A[i], B[i])
    edges.append(temp)



for edge in edges:
    sor = edge[0]
    tar = edge[1]
    g[sor, tar, 'adv','pub'] = 1



#plt.xlabel("X-axis Label")
#plt.ylabel("Y-axis Label")

draw(g, layergap=2.8,
    nodeLabelRule={})

plt.title('Network of advertisers and publishers')
#
