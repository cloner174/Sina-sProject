import matplotlib.pyplot as plt
import pandas as pd

link_data = pd.read_csv("data/link_dataFinal.csv")
node_data =  pd.read_csv("output/node_data.csv")

layr1Node = node_data.iloc[:571, 1]
layr2Node = node_data.iloc[571:, 1]

from 