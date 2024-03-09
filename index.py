#
import pandas as pd
from pymnet import *
import matplotlib.pyplot as plt
import time
import re
#datanode = pd.read_csv('data/node.csv')
#datalink = pd.read_csv('data/links.csv')


class Sina:
    
    
    
    def __init__(self, dataNodes: dict, dataLinkes: dict, data_adv , data_pub):
        
        self.datanode = dataNodes
        self.datalink = dataLinkes
        self.advers = data_adv
        self.publishs = data_pub
    
    
    
    
    
    
    def main(self, nameAttr: str,# nameAttr2: str, nameAttr3: str,
             LogicsForNodes: str = 'type',  name: str = 'name', id: str = 'id', links_sorce: str = 'source', 
             links_target: str = 'target'):
        
        
        nodes = self.datanode
        links = self.datalink
        
        
        linkSorc = list( links[links_sorce]  )
        linkTar = list( links[links_target] )
        logicnode = list( nodes[LogicsForNodes] )

        #generete_random = np.random.randint(10000)
        
        layerOneNodesNames = []
        layerTwoNodesNames = []
        layerOneNodesIndexIDs = []
        layerTwoNodeIndexIDs = []
        attrLAYER1 = []
        attrLAYER2 = []
        #attr_2_LAYER1 = []
        #attr_2_LAYER2 = []
        #attr_3_LAYER1 = []
        #attr_3_LAYER2 = []
        trash_ = []
        
        for i in range( len( logicnode )):
            
            temp_name= nodes[name][i]
            temp_id = nodes[id][i]
            temp_TrueFalse = nodes[LogicsForNodes][i]
            temp_attrr1 = nodes[nameAttr][i]
            #temp_attrr2 = nodes[nameAttr2][i]
            #temp_attrr3 = nodes[nameAttr3][i]
            
            if temp_TrueFalse == True:
                
                layerOneNodesNames.append( temp_name )
                layerOneNodesIndexIDs.append( temp_id)
                
                attrLAYER1.append( { str(nameAttr) : temp_attrr1 } )
                #attr_2_LAYER1.append( { str(nameAttr2) : temp_attrr2 } )
                #attr_3_LAYER1.append( { str(nameAttr3) : temp_attrr3 } )    
                
            
            elif temp_TrueFalse == False:
                
                layerTwoNodesNames.append( temp_name )
                layerTwoNodeIndexIDs.append( temp_id )
                
                attrLAYER2.append( { str(nameAttr) : temp_attrr1 } )
                #attr_2_LAYER2.append( { str(nameAttr2) : temp_attrr2 } )
                #attr_3_LAYER2.append( { str(nameAttr3) : temp_attrr3 } )              
                
            else:
                
                trash_.append( (temp_name,temp_id) )
        
        #attr_layer1 = [ attrLAYER1, attr_2_LAYER1, attr_3_LAYER1 ]
        #attr_layer2 = [attrLAYER2, attr_2_LAYER2, attr_3_LAYER2]
        attr_layer1 = attrLAYER1
        attr_layer2 = attrLAYER2
        
        
        Edges = []
        for i in range( len( linkSorc )):
            
            tempsorc = linkSorc[i]
            temptar = linkTar[i]
            
            tempedge = ( tempsorc, temptar )
            Edges.append( tempedge ) 
        
        
        return layerOneNodesNames, layerOneNodesIndexIDs, layerTwoNodesNames, layerTwoNodeIndexIDs, Edges,  attr_layer1, attr_layer2#, trash_
    
    
    #layer one -->> a -->> publishers
    #layer two -->> b -->> advers    
    
    def Re(self):
        
        A, B, c_, d_, e_, f_, ga_ = self.main()
        
        layerOneID = []
        for i in range( len( A ) ):
            
            aaAA = A[i]
            temp = re.search( '\d++', aaAA )
            temp2 = temp.group()
            layerOneid = int(temp2)
            A[i] = layerOneid
            layerOneID.append( layerOneid)
            
        layerTwoID = []
        for j in range( len( B ) ):
            
            bbBB = B[j]
            temp = re.search( '\d++', bbBB )
            temp2 = temp.group()
            layertwoid = int(temp2)
            B[j] = layertwoid
            layerTwoID.append( layertwoid)
        
        
        return layerOneID, layerTwoID, A , B
        
                  
             
            
            
    
    
    #  #   ##     ##      #   #       ##    ##      Visulize and more . . . ! . . .  ## # # #        # #
    #print(layerOneColors) -->> 'blue', 'blue', 'blue', . . .. 
    
    
    def GraphCreate(fully_Interconnect = False, Aspect = 1,
                    layer_one_name = 'Advertisers', 
                    layer_two_name = 'Publishers'):
        
        print( " Getting things Ready . . . ")
        time.sleep(2)
        
        g = MultilayerNetwork(aspects = Aspect,
                          fullyInterconnected = fully_Interconnect)
        
        print( "Seccessfully Create The Graph Object !")
        time.sleep(2)
        print( " Adding layers . . . ")
        time.sleep(2)
        
        g.add_layer(layer_one_name)
        g.add_layer(layer_two_name)
        
        print(" Done !")
        time.sleep(2)
        
        print(g.get_layers())
        
        time.sleep(2)
        
        return g
    
    
    
    def finall(self):
        
        L1N, L1id , L2N , L2id, LiL, Atr1 , Atr2 = self.main()
        
        #N_a = input("Meghdar Avalie Baraye -a- . . \n")
        #N_a = int(N_a)
        #V_a = input( "Meghdar Avalie Baraye -a- . . \n ")
        #V_a = int(V_a)
        #N_b = input("Meghdar Avalie Baraye -b- . . \n")
        #N_b = int(N_b)
        #V_b = input( "Meghdar Avalie Baraye -b- . . \n ")
        #V_b = int(V_b)
        
        firstA = []
        
        for i in range( len( L1N ) ):
            
            name = L1N[i]
            id = L1id[i]
            
            for J in name:
                
                j = J[0] #avali
                
                if temp == j:
                    
                    firstA.append()
        
        
    def Add_nodes_to_GraphObject(self):
        
        g = self.GraphCreate()
        
        for i in self.a:
        
            g.add_node(i, 'advertisers')
            
            
        for j in self.b:
            
            g.add_node(i, 'publishers')
            
            
            
    def add_Links(self):
        
        layerOneLinks = []
        layerTwoLinks = []
        InterConnectedLinks = []
        
        
        for j in range( len( self.c ) ):
    
            edge = self.c[j]
            
            temp1 = edge[0]
            temp2 = edge[1]
            
            if temp1 in self.a:
                
                if temp2 in self.a:
                
                    layerOneLinks.append(edge)
                
                else:
                    
                    if temp2 in self.b:
                        
                        InterConnectedLinks.append(edge)
            
            elif temp1 in self.b:
        
                if temp2 in self.b:
                    
                    layerTwoLinks.append( edge )
                
                else:
                   
                    if temp2 in self.a:
                        
                        InterConnectedLinks.append(edge)
        

print( "\n len( layerTwoLinks) -->> ", len( layerTwoLinks),  "\n len( layerOneLinks) -->> ",  len( layerOneLinks),
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
    
    if edgeSource in a:
        
        g[edgeSource, edgeTarget, 'publishers','advertisers'] = 1
        
    else:
        
        g[edgeSource, edgeTarget, 'advertisers','publishers'] = 1



draw(g, layergap=2.5,
    nodeLabelRule={}, show=True)

plt.title('Network of advertisers and publishers')