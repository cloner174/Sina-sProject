from pymnet import *
import matplotlib.pyplot as plt
import pandas as pd
import re






advertiser = pd.read_csv('data/advertisers.csv' )

publisher = pd.read_csv('data/publishers.csv')

links = pd.read_csv('data/links.csv')

nodes =  pd.read_csv('data/node.csv')


advertiser.head()
links.head()
nodes.head()
publisher.head()

link = dict(links)
node = dict(nodes)

link.keys()
node.keys()


names = node['name']



links = pd.DataFrame(links)


links.head()
links.columns
advertissers.columns
publishers.columns
interactions.columns




publishers = publishers.set_axis(["rowNum", "ID", "PublisherID", 'TotalLikes','TotalViews','Price',
                                  'TotalInteractions','TotalReach','PublisherPrice',
                                  'MediaPlanPrice','HasPaidPartnership','MediaPlanContentType',
                                  'Media.PlanCampaignType','MediaPlanIsVip','MediaCategoryID',
                                  'IsInfluencer','IsPrivate','IsCelebrity','MediaCategoryTitle'],axis= 'columns' )


advertisers = advertissers.set_axis([ 'rowNum', 'ID', 'AdvertiserID', 'MediaPlansCategories', 
                                      'CampaignCategoryID', 'CampaignType','ManagerID', 'ManagementPercentFee', 'IsUtmEnabled', 
                                      'PublishPeriodStart','Budget','QualityOfAdvertise','QualityOfBusiness', 'IsOfficial', 
                                      'IsShortLinkEnabled','IsCompetitionOrHasAward'], axis= "columns")




nodeAdvers = list( advertisers.loc[:, "CampaignCategoryID"].unique() )
nodePublishs = list( publishers.loc[:, "PublisherID"].unique() )

links_ = list(links.loc[:,'source'].unique())





#for advertise in nodeAdvers:
#    
#    g.add_node( advertise, "advertisers")
#for publisher in nodePublishs:
#    
#    g.add_node( publisher, "publishers")
#draw( g, layergap= 2.5)
#plt.show()

def interAction(nodes1: list, nodes2: list, base: dict, NameOfnodes1IDinBase: str,  NameOfNodes2IDinBase: str) :
    
    nodes1ID = []
    nodes2ID = []
    
    for i in range( len( base[NameOfnodes1IDinBase] )):
        
        temp = base[NameOfnodes1IDinBase][i]
        temp2 = base[NameOfNodes2IDinBase][i]
        
        if temp in nodes1:
            
            nodes1ID.append(temp)
            nodes2ID.append(temp2)
                 
                
    if len( nodes1ID) == len(nodes2ID):
        
        return nodes1ID, nodes2ID
    
    else:
        
        raise TypeError( "\n  There WAS a PROBLEM some WHERE ,, len of two OBJECT is NOT the SAME \n ")



interactions = interactions.set_axis( [ 'ID',  'CampaignID', 'AdvertiserID', 'PublisherID'], axis= 'columns')

dictinteractions = dict(interactions)



node_adver, node_pusbli = interAction(nodeAdvers, nodePublishs, dictinteractions, 'AdvertiserID', 'PublisherID')



g = MultilayerNetwork(aspects=1,
                      fullyInterconnected=False)


g.add_layer('advertisers')
g.add_layer('publishers')



for i in range(len(node_adver)):
    
    temp1 = node_adver[i]
    temp2 = node_pusbli[i]
    
    g[ temp1, temp2, 'advertisers', 'publishers'] = 1




draw(g, layergap=2.5,
    nodeLabelRule={})

plt.title('Network of advertisers and publishers')
plt.show()


#for i in range( len( advertisers.loc[:, ])):
#    
#    if 