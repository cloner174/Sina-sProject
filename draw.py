#                         # #          #          In the name of God   # #
#
#
#
import pandas as pd

link_data = pd.read_csv("data/link_dataFinal.csv")
node_data =  pd.read_csv("output/node_data.csv")

layr1Node = node_data.iloc[:571, 1]
layr2Node = node_data.iloc[571:, 1]

from index import Visualize

#hint:
#def __init__(self, data_nodes, data_linkes, Advers_nod , Pub_nod)

test = Visualize(node_data,  link_data, layr1Node, layr2Node)

test.Run_()