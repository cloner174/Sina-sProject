#
import pandas as pd
from pymnet import *
import matplotlib.pyplot as plt
import time
import re



class Sina:
    
    
    
    def __init__(self, dataNodes, dataLinkes, data_adv, data_pub):
        
        self.datanodeDF = dataNodes.copy()
        self.datalinkDF = dataLinkes.copy()
        self.adversDF = data_adv.copy()
        self.publishsDF = data_pub.copy()
        
        self.datanode = dict( dataNodes )
        self.datalink = dict( dataLinkes )
        self.advers = dict( data_adv )
        self.publishs = dict( data_pub )
    
    
    
    def Re(self):
        
        
        A = self.advers
        B = self.publishs
        
        Akeys = list( A.keys() )
        Bkeys = list( B.keys() )
        
        
        for i in range( len( Akeys )):
            
            temp = str( Akeys[i] )
            
            temp1 = temp.lower()
            tempp = re.search( r'advertiser', temp1 )
            
            if tempp != None:
                
                temppp = re.search( r'id', temp1)
                
                if temppp != None :
                    
                   AdverName_main = temp
                   Adver_index_in_Akeys = i
            
        
        for j in range( len( Bkeys )):
            
            temp = str( Bkeys[j] )
            
            temp1 = temp.lower()
            tempp = re.search( r'publisher', temp1 )
            
            if tempp != None:
                
                temppp = re.search( r'id', temp1)
                
                if temppp != None :
                    
                   PublishName_main =  temp
                   
                   Publish_index_in_Bkeys = j
                
        
        C = self.datanodeDF.copy()
        
        for i in range( C.shape[0] ):
            
            aaAA = C.loc[i, 'name']
            temp = re.search( '\d++', aaAA )
            temp2 = temp.group()
            temp3 = int(temp2)
            C.loc[i, 'name'] = temp3
        
        
        return AdverName_main, Adver_index_in_Akeys, PublishName_main, Publish_index_in_Bkeys, C
    
    
    
    
    
    def Layer_Split(self, nameAttr: str,# nameAttr2: str, nameAttr3: str,
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
            
            if temp_TrueFalse == False:
                
                layerOneNodesNames.append( temp_name )
                layerOneNodesIndexIDs.append( temp_id)
                
                attrLAYER1.append( { str(nameAttr) : temp_attrr1 } )
                #attr_2_LAYER1.append( { str(nameAttr2) : temp_attrr2 } )
                #attr_3_LAYER1.append( { str(nameAttr3) : temp_attrr3 } )    
                
            
            elif temp_TrueFalse == True:
                
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
    
    def main( self, att:str = None, all_ = False ):
        
        if att:
            att = att
        else:
            att = 'color'
        
        nameOfColomnOfAdvertisersIDinAllSources, indexOfIt, ssame_for_publishers, pub_indexes, nods = self.Re()
        
        lyrAdverNodName,lyrAdverNodIndxID,lyrPubNodName,lyrPubNodIndxID,Edges,colorAdvrLyr1,colorPubLyr2 = self.Layer_Split(att)
        
        ValidNodLayer1Advers = []
        ValidNodLayer1Advers2 = []
        ValidNodLayer1Advers3 = []
        for i in range( len( lyrAdverNodName )) :
            
            temp = lyrAdverNodName[i]
            temp2 = lyrAdverNodIndxID[i]
            temp3 = colorAdvrLyr1[i]
            
            vaLIdMAin = self.adversDF
            
            if temp in vaLIdMAin.loc[:, nameOfColomnOfAdvertisersIDinAllSources] :
                
                ValidNodLayer1Advers.append( temp )
                ValidNodLayer1Advers2.append( temp2 )
                ValidNodLayer1Advers3.append( temp3 )
        
        
        ValidNodLayer1Pub = []
        ValidNodLayer1Pub2 = []
        ValidNodLayer1Pub3 = []
                
        for j in range( len( lyrPubNodName ) ) :
            
            temp = lyrPubNodName[j]
            temp2 = lyrPubNodIndxID[j]
            temp3 = colorPubLyr2[j]
            
            VaLIDs_maIN = self.publishsDF
            
            if temp in VaLIDs_maIN.loc[:, ssame_for_publishers] :
                
                ValidNodLayer1Pub.append( temp)
                ValidNodLayer1Pub2.append( temp2 )
                ValidNodLayer1Pub3.append( temp3 )
        
        
        #for i in Edges:
        #    
        #    for j in i:
        #        
        #        j_ = j[0]
        #        j__ = j[1]
        #        
        #        if j_ in ValidNodLayer1Advers2:
        #            
        #            if j_ in ValidNodLayer1Pub2:
                        
                        
        
        
        if all_ != False:
            
            return ValidNodLayer1Advers,ValidNodLayer1Advers2,ValidNodLayer1Advers3, ValidNodLayer1Pub,ValidNodLayer1Pub2,ValidNodLayer1Pub3
        else:
            
            return ValidNodLayer1Advers, ValidNodLayer1Pub, Edges
    
    
    
    def modify_links(self):
        
        
        a, b, c = self.main() 
        
        
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
    
    
    def add_links(self) :
        
        layerOneLinks, layerTwoLinks, InterConnectedLinks , a = self.modify_links()
        
        g = self.GraphCreate()
        
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
    
    def Run_(self):
        
        g = self.add_links()
        
        return g

#end#