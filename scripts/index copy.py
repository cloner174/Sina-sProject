#
import pandas as pd
from pymnet import *
import matplotlib.pyplot as plt
import time


datanode = pd.read_csv('data/node.csv')
datalink = pd.read_csv('data/links.csv')

print( "\n  datanode.head()  --:: \n", datanode.head(), "\n" )
time.sleep(2)
print(  "\n  datalink.head()  --:: \n", datalink.head() , "\n")
time.sleep(2)




Anode = list( datanode.loc[:,'id'] )
AlinkSorc = list( datalink.loc[:, 'source'] )
AlinkTar = list( datalink.loc[:, 'target'])
Acolornode = list( datanode.loc[:, 'color'])
Alogicnode = list( datanode.loc[:, 'type'])




def main(nodes1: list, layer1: str, nodes2: list, layer2: str , attrColsRangeStartNodes1: int,attrColsRangeEndsNodes1:int,
         attrColsRangeStartNodes2: int,attrColsRangeEndsNodes2:int):
    
    nods1 = nodes1.copy()
    nods2 = nodes2.copy()
    
    layerOneNodes = []
    layerTwoNodes = []
    layerOne_attr = {}
    layerTwo_attr = {}
    layerOne_colors = {}
    layerTwo_colors = {}
    
    
    for i in range( len( nods1 )):
        
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


print("\n  layerOneNodes -->> ", len(layerOneNode),  "\n  layerTwoNodes -->> ", len(layerTwoNode), "\n",
      " layerOneColors -->> ", len(layerOneColors), "\n"," layerTwoColors -->> ", len(layerTwoColors), "\n",
      " IDcolors   &&  edges Final -->> ", len(IDcolors),len(edgesFinal), "\n",
      " type(layerOneNode[10]&&layerTwoNode[10])&&layerOneColor[10])-->>", type(layerOneNode[10]), type(layerTwoNode[10]),type(layerOneColors[10]), 
      "\n  type(layerTwoColors[10] && IDcolors && edgesFinal[10]) -->> ", type(layerTwoColors[10]), type(IDcolors), type(edgesFinal[10]), "\n",
      "edgesFinal[0] = ", edgesFinal[0], "\n edgesFinal[0] = " , edgesFinal[22] )


time.sleep(3)

#  #   ##     ##      #   #       ##    ##      Visulize and more . . . ! . . .  ## # # #        # #


g = MultilayerNetwork(aspects=1,
                      fullyInterconnected=False)


g.add_layer('advertisers')
g.add_layer('publishers')
g.add_layer()
g.add_node()
#print(layerOneColors) -->> 'blue', 'blue', 'blue', . . .. 


for i in layerOneNode:
    
    g.add_node(i, 'publishers')


for i in layerTwoNode:
    
    g.add_node(i, 'advertisers')


layerOneLinks = []
layerTwoLinks = []
InterConnectedLinks = []
for j in range( len( edgesFinal ) ):
    
    edge = edgesFinal[j]
    
    temp1 = edge[0]
    temp2 = edge[1]
    
    if temp1 in layerOneNode:
        
        if temp2 in layerOneNode:
        
            layerOneLinks.append(edge)
        
        else:
            
            if temp2 in layerTwoNode:
                
                InterConnectedLinks.append(edge)
    
    elif temp1 in layerTwoNode:
        
        if temp2 in layerTwoNode:
            
            layerTwoLinks.append( edge )
        
        else:
            
            if temp2 in layerOneNode:
                
                InterConnectedLinks.append(edge)


print( "\n len( layerTwoLinks) -->> ", len( layerTwoLinks),  "\n len( layerTwoLinks) -->> ",  len( layerOneLinks),
      "\n len( InterConnectedLinks) -->> ",len( InterConnectedLinks) )

time.sleep(2)


#draw(g)

#plt.savefig('output/Figure_1.png')
#plt.show()

print( "\n  You can Find this Figure and also all others in -output- folder  \n")

time.sleep(2)


for edge in layerOneLinks:
    
    edgeSource = edge[0]
    edgeTarget = edge[1]
    
    g[edgeSource, edgeTarget, 'publishers','publishers'] = 1

for edge in layerTwoLinks:
    
    edgeSource = edge[0]
    edgeTarget = edge[1]
    
    g[edgeSource, edgeTarget, 'advertisers','advertisers'] = 1

for edge in InterConnectedLinks:
    
    edgeSource = edge[0]
    edgeTarget = edge[1]
    
    if edgeSource in layerOneNode:
        
        g[edgeSource, edgeTarget, 'publishers','advertisers'] = 1
        
    else:
        
        g[edgeSource, edgeTarget, 'advertisers','publishers'] = 1



draw(g, layergap=2.6,
    nodeLabelRule={})


plt.title('Network of advertisers and publishers')
plt.show()


for i in 




