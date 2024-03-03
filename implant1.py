import networkx as nx
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier

# Assuming link_data and node_data are your data frames
# Adjust column names based on your actual data frame structure

# Create a graph
G = nx.Graph()

# Add nodes with attributes from node_data
for _, node_row in node_data.iterrows():
    G.add_node(node_row['id'], name=node_row['name'], type=node_row['type'], color=node_row['color'])

# Add edges from link_data
for _, link_row in link_data.iterrows():
    G.add_edge(link_row['source'], link_row['target'], key=link_row['key'])

# Feature extraction
# Here you should extract relevant features for link prediction
# Replace this with your own feature extraction logic
def extract_features(G, edges):
    features = []
    for edge in edges:
        source, target = edge
        # Replace this with your own feature extraction logic based on node attributes, graph structure, etc.
        feature = {'common_neighbors': len(list(nx.common_neighbors(G, source, target)))}
        features.append(feature)
    return features

# Generate positive and negative examples for training
non_edges = list(nx.non_edges(G))
edges = list(G.edges)

# Set labels for positive and negative examples
labels = [1] * len(edges) + [0] * len(non_edges)

# Combine positive and negative examples
all_edges = edges + non_edges

# Extract features for each edge
features = extract_features(G, all_edges)

# Convert features to DataFrame
features_df = pd.DataFrame(features)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features_df, labels, test_size=0.2, random_state=42)

# Train a classifier (e.g., RandomForestClassifier)
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Predict on the test set
y_pred = clf.predict_proba(X_test)[:, 1]

# Evaluate the performance (e.g., using ROC-AUC)
roc_auc = roc_auc_score(y_test, y_pred)
print("ROC-AUC Score:", roc_auc)
