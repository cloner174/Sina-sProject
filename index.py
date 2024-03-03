#
import pandas as pd
from pymnet import *
import matplotlib.pyplot as plt



datanode = pd.read_csv('data/node.csv')
datalink = pd.read_csv('data/links.csv')

print( datanode.head() )
print( datalink.head() )



Anode = list( datanode.loc[:,'id'] )
AlinkSorc = list( datalink.loc[:, 'source'] )
AlinkTar = list( datalink.loc[:, 'target'])
Acolornode = list( datanode.loc[:, 'color'])
Alogicnode = list( datanode.loc[:, 'type'])




def main(nodes, edgesSource, edgesTarget, ColoursForNodes, LogicsForNodes):
    
    nods = nodes.copy()
    esorc = edgesSource.copy()
    etar = edgesTarget.copy()
    colors_ = ColoursForNodes.copy()
    logics_ = LogicsForNodes.copy()
    
    layerOneNodes = []
    layerTwoNodes = []
    layerOneColors = []
    layerTwoColors = []
    
    for i in range( len( nods )):
        
        temp = logics_[i]
        if temp == True:
            
            layerOneNodes.append( nods[i] )
            layerOneColors.append( colors_[i] )
        
        elif temp == False:
            
            layerTwoNodes.append( nods[i] )
            layerTwoColors.append( colors_[i] )
        
        else:
            
            continue
        
    Edges = []
    for i in range( len( esorc )):
        
        tempsorc = esorc[i]
        temptar = etar[i]
        
        tempedge = ( tempsorc, temptar )
        Edges.append( tempedge )
    
    
    
    IDcolor = {}
    for i in range( len( layerOneNodes )):
        
        temp1 = int( layerOneNodes[i] )
        temp2 = layerOneColors[i]
        
        IDcolor.update( { temp1 : temp2 })
    
    
    for i in range( len( layerTwoNodes )):
        
        temp1 = int( layerTwoNodes[i] )
        temp2 = layerTwoColors[i]
        
        IDcolor.update( { temp1 : temp2 })
    
    return layerOneNodes, layerTwoNodes, layerOneColors,  layerTwoColors, IDcolor, Edges




layerOneNode, layerTwoNode, layerOneColors, layerTwoColors, IDcolors, edgesFinal = main( Anode, AlinkSorc, AlinkTar, Acolornode, Alogicnode )

print(len(layerOneNode), len(layerTwoNode), 
      len(layerOneColors),len(layerTwoColors),
      len(IDcolors),len(edgesFinal),
      type(layerOneNode[10]), type(layerTwoNode[10]),type(layerOneColors[10]), type(layerTwoColors[10]),
      type(IDcolors), type(edgesFinal[10]), edgesFinal[0], edgesFinal[22])



#  #   ##     ##      #   #       ##    ##      Visulize and more . . . ! . . .  ## # # #        # #


g = MultilayerNetwork(aspects=1,
                      fullyInterconnected=False)


g.add_layer('advertisers')
g.add_layer('publishers')

#print(layerOneColors) -->> 'blue', 'blue', 'blue', . . .. 


for i in layerOneNode:
    
    g.add_node(i, 'publishers')
    
    
for i in layerTwoNode:
    
    g.add_node(i, 'advertisers')


layerOneLinks = []
layerTwoLinks = []
for j in range( len( edgesFinal ) ):
    
    edge = edgesFinal[j]
    
    temp1 = edge[0]
    temp2 = edge[1]

    if temp1 in layerOneNode:
        
        if temp2 in layerOneNode:
        
            layerOneLinks.append(edge)
    else:
        layerTwoLinks.append( edge )

print( len( layerTwoLinks), len( layerOneLinks), len( edgesFinal) )

