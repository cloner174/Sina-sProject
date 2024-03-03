from pyvis.network import Network
import json


with open('result.json', 'r') as file:
    data = json.load(file)

data.pop(list(data.keys())[0])
data.pop(list(data.keys())[0])
data.pop(list(data.keys())[0])

# Assuming data is your dictionary
nodes = data['nodes']
links = data['links']

# Create a network
net = Network(height="800px", width="100%", notebook=True)

# Add nodes
for node in nodes:
    net.add_node(node['id'], label=node['name'], title=f"Type: {node['type']}, Color: {node['color']}")

# Add edges
for link in links:
    net.add_edge(link['source'], link['target'], title=link.get('type', ''))

# Show network
net.show("graph.html")
