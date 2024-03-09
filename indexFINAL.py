from pymnet import *
import matplotlib.pyplot as plt


g = MultilayerNetwork(aspects=1,
                      fullyInterconnected=False)


g.add_layer('advertisers')
g.add_layer('publishers')


import pandas as pd

advertissers = pd.read_csv('data/advertisers.csv' )

publishers = pd.read_csv('data/publishers.csv')




advertissers.head()
publishers.head()














