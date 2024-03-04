

for i in layer1:
    g.add_node(i, 'publishers')


for i in layer2:
    g.add_node(i, 'advertisers')



links1 = []
links2 = []
links12 = []

for j in range( len( edgesFinal ) ):
    edge = edgesFinal[j]
    temp1 = edge[0]
    temp2 = edge[1]
    if temp1 in layer1:
        if temp2 in layer1:
           links1.append(edge)  
        else:
            if temp2 in layer2:
                links12.append(edge)
    elif temp1 in layer2:
        if temp2 in layer2:
            links2.append( edge )
        else:
            if temp2 in layer1:
                links12.append(edge)

for edge in links1:
    
    edgeSource = edge[0]
    edgeTarget = edge[1]
    
    g[edgeSource, edgeTarget, 'advertisers','advertisers'] = 1

for edge in links2:
    
    edgeSource = edge[0]
    edgeTarget = edge[1]
    
    g[edgeSource, edgeTarget, 'publishers','publishers'] = 1

for edge in links12:
    
    edgeSource = edge[0]
    edgeTarget = edge[1]
    
    if edgeSource in layer1:
        
        g[edgeSource, edgeTarget, 'publishers','advertisers'] = 1
        
    else:
        
        g[edgeSource, edgeTarget, 'advertisers','publishers'] = 1






draw(g, layergap=2.6,
    nodeLabelRule={}, layout = 'fr', show = True, alignedNodes = False)

plt.title('Network of advertisers and publishers')