
        

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

#datanode = pd.read_csv('data/node.csv')
#datalink = pd.read_csv('data/links.csv')