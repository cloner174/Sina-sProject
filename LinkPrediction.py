import networkx as nx
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier

# Assuming link_data and node_data are your data frames
# Adjust column names based on your actual data frame structure
node_data = pd.read_csv("data/node.csv")
link_data = pd.read_csv("data/links.csv")
advers = pd.read_csv("data/advertisers.csv")
pubs = pd.read_csv("data/publishers.csv")

from index import Sina

mine = Sina(node_data, link_data, advers, pubs)
AdvColName, AdvColIndex, PubColName, PubColIndex, RenamedNodeData = mine.Re()
len(RenamedNodeData)

Uadv = list(advers.iloc[:,AdvColIndex].unique())
Upubs = list( pubs.iloc[:, PubColIndex ].unique() )
NodeData = RenamedNodeData.copy()
NodeData1 = RenamedNodeData.copy()
num_ = 0
while num_ < NodeData.shape[0]:
    
    temp = NodeData.loc[num_,'name']
    
    if temp in Uadv:
        num_ += 1
    
    else:
        
        if temp in Upubs:
            num_ += 1
        
        else:
            
            if num_ == NodeData1.shape[0]:
                break
            
            else:
                
                NodeData1 = NodeData1.drop(num_)
                num_ += 1


node_data = NodeData1.set_axis( [ i for i in range(NodeData1.shape[0])] , axis = 0)
allnodes_id = list( node_data.loc[:,'id'] )


#node_data.to_csv('node_data.csv')#
##node_data.to_csv('output/node_data.csv')##
###node_data.to_csv('Rside/data/node_data.csv')###


##


link_data = pd.read_csv("data/link_dataFinal.csv")



# Create a graph
G = nx.Graph()

# Add nodes with attributes from node_data
for _, node_row in node_data.iterrows():
    G.add_node(node_row['id'], name=node_row['name'], type=node_row['type'], color=node_row['color'])

# Add edges from link_data
for _, link_row in link_data.iterrows():
    G.add_edge(link_row['source'], link_row['target'], key=link_row['key'])


# extract relevant features for link prediction
def extract_features(G, edges):
    features = []
    for edge in edges:
        source, target = edge
        feature = {'common_neighbors': len(list(nx.common_neighbors(G, source, target)))}
        features.append(feature)
    return features

# Generate positive and negative examples for training
non_edges = list(nx.non_edges(G))
edges = list(G.edges)


# Set labels for positive and negative examples
labels = [1] * len(edges) + [0] * len(non_edges)


# Combine positive and negative
all_edges = edges + non_edges

# Extract features for each edge
features = extract_features(G, all_edges)

# Convert to DataFrame
features_df = pd.DataFrame(features)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(features_df, labels, test_size=0.2, random_state=42)

# Train a classifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Predict on the test
y_pred = clf.predict_proba(X_test)[:, 1]

# Evaluate (using ROC-AUC)
roc_auc = roc_auc_score(y_test, y_pred)
print("ROC-AUC Score: ", roc_auc)

# ROC-AUC Score: 0.9683730947010214