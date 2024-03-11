#
from pymnet import *
import time


class Visualize:
    
    
    
    def __init__(self, data_nodes, data_linkes, Advers_nod , Pub_nod):
        
        self.data_nodes = data_nodes
        self.data_linkes = data_linkes
        self.Advers_nod = Advers_nod
        self.Pub_nod = Pub_nod
    
    
    
    def modify_links(self):
        
        print( " Getting things Ready . . . ")
        
        a = self.Advers_nod
        b = self.Pub_nod
        c = self.data_linkes
        
        layerOneLinks = []
        layerTwoLinks = []
        InterConnectedLinks = []
        
        for j in range( c.shape[0] ):
    
            edge = tuple( ( (c.loc[j, 'source']), (c.loc[j, 'target']) ) )
            
            temp1 = edge[0]
            temp2 = edge[1]
            
            if temp1 in a:
                
                if temp2 in a:
                
                    layerOneLinks.append(edge)
                
                else:
                    
                    if temp2 in b:
                        
                        InterConnectedLinks.append(edge)
            
            elif temp1 in b:
        
                if temp2 in b:
                    
                    layerTwoLinks.append( edge )
                
                else:
                   
                    if temp2 in a:
                        
                        InterConnectedLinks.append(edge) 
                    
                
        return layerOneLinks, layerTwoLinks, InterConnectedLinks
    
    
    
    def GraphCreate(fully_Interconnect = False, Aspect = 1,
                    layer_one_name = 'Advertisers', 
                    layer_two_name = 'Publishers'):
        
        print( " Starting to Create Graph . . . ")
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
    
    
    def add_links(self, g ,layerOneLinks, layerTwoLinks, InterConnectedLinks) :
        
        
        for edge in layerOneLinks:
            
            edgeSource = edge[0]
            edgeTarget = edge[1]
            
            g[edgeSource, edgeTarget, 'advertisers','advertisers'] = 1
        
        for edge in layerTwoLinks:
            
            edgeSource = edge[0]
            edgeTarget = edge[1]
            
            g[edgeSource, edgeTarget, 'publishers','publishers'] = 1
        
        for edge in InterConnectedLinks:
            
            edgeSource = edge[0]
            edgeTarget = edge[1]
            
            g[edgeSource, edgeTarget, 'advertisers','publishers'] = 1
            
        
        return g
    
    
    def Run_(self ):
        
        print(" Running !")
        time.sleep(5)
        layerOneLinks, layerTwoLinks, InterConnectedLinks = self.modify_links()
        
        Gtemp = self.GraphCreate()
        print("Almost Finish !")
        time.sleep(2)
        G = self.add_links( Gtemp,layerOneLinks, layerTwoLinks, InterConnectedLinks )
        
        print( " Your Gragh is Now Ready To use .")
        time.sleep(2)
        
        inn_ = input( "\n  Type  - draw - to start drawing OR press inter to Return Graph Object " )
        time.sleep(2)
        if inn_ == "":
            
            return G
        elif inn_ == "draw":
            
            draw(G, layout =  "spring", layergap=2.5,
                 nodeLabelRule={}, show=True, )
            exit()
        else:
            raise KeyError( "\n Invalid Command \n")
        
    
#end#