#
import pandas as pd
from pymnet import *
import matplotlib.pyplot as plt
import time
import re



class Sina:
    
    
    
    def __init__(self, dataNodes, dataLinkes, ValidNodLayer1Advers, ValidNodLayer1Pub, Edges):
        
        self.datanodeDF = dataNodes
        self.datalinkDF = dataLinkes
        self.ValidNodLayer1Advers = ValidNodLayer1Advers
        self.ValidNodLayer1Pub = ValidNodLayer1Pub
        self.Edges = Edges

    
    
    
    def modify_links(self):
        
        
        a = self.ValidNodLayer1Advers
        b = self.ValidNodLayer1Pub
        c = self.Edges
        
        
        layerOneLinks = []
        layerTwoLinks = []
        InterConnectedLinks = []
        
        
        for j in range( len( c ) ):
    
            edge = c[j]
            
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
                    
                
        return layerOneLinks, layerTwoLinks, InterConnectedLinks, a
    
    
    
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
    
    
    def add_links(self, g ,layerOneLinks, layerTwoLinks, InterConnectedLinks , a) :
        
        
        
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
        
        return g
    
    #  #   ##     ##      #   #       ##    ##      Visulize and more . . . ! . . .  ## # # #        # #
    #print(layerOneColors) -->> 'blue', 'blue', 'blue', . . .. 
        
    def Add_nodes_to_GraphObject(self):
        
        pass
    #   Not Implanted
    #    g = self.GraphCreate()
    #    
    #    a, b = self.main()
    #    
    #    for i in self.a:
    #    
    #        g.add_node(i, 'advertisers')
    #        
    #        
    #    for j in self.b:
    #        
    #        g.add_node(j, 'publishers')
    #    
    
    def Run_(self ):
        
        
        layerOneLinks, layerTwoLinks, InterConnectedLinks = self.modify_links()
        
        Gtemp = self.GraphCreate()
        
        G = self.add_links( Gtemp,layerOneLinks, layerTwoLinks, InterConnectedLinks, self.ValidNodLayer1Advers )
        
        return G

#end#