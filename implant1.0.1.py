import networkx as nx
import matplotlib.pyplot as plt

# Assuming link_data and node_data are your data frames
# Adjust column names based on your actual data frame structure

# Create a graph
G = nx.Graph()

# Add nodes with attributes from node_data
for _, node_row in node_data.iterrows():
    # Check if the node exists before adding
    if not G.has_node(node_row['id']):
        G.add_node(node_row['id'], name=node_row['name'], type=node_row['type'], color=node_row['color'])

# Add edges from link_data
for _, link_row in link_data.iterrows():
    # Check if the edge exists before adding
    if not G.has_edge(link_row['source'], link_row['target']):
        G.add_edge(link_row['source'], link_row['target'], key=link_row['key'])

# Visualize the graph (optional)
pos = nx.spring_layout(G)  # Choose a layout algorithm
nx.draw(G, pos, with_labels=True, font_weight='bold', node_color=node_data['color'])
plt.show()
