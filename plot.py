import matplotlib.pyplot as plt
import networkx as nx

# Create a bipartite graph
B = nx.Graph()

# Add nodes with the bipartite attribute
left_nodes = ["A1", "A2", "A3"]
right_nodes = ["B1", "B2", "B3"]
B.add_nodes_from(left_nodes, bipartite=0)
B.add_nodes_from(right_nodes, bipartite=1)

# Add edges between nodes
edges = [("A1", "B1"), ("A2", "B1"), ("A3", "B2"), ("A1", "B3"), ("A2", "B2")]
B.add_edges_from(edges)

# Position nodes using bipartite_layout
pos = nx.bipartite_layout(B, left_nodes)

# Draw the graph
nx.draw(B, pos, with_labels=True, node_color=['lightblue' if node in left_nodes else 'lightgreen' for node in B.nodes()])
plt.show()
