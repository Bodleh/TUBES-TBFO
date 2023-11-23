import networkx as nx
import matplotlib.pyplot as plt
# Create a directed graph
G = nx.DiGraph()

G.add_node("START")
G.add_node("HTML")
G.add_edge("START", "HTML")

with open('tf.txt', 'r') as file :
    lines = file.readlines()

# from_state = input("From State: ").upper()
# to_state = input("To State: ").upper()
states = ["START", "HTML"]

for line in lines :
    line = line.split()
    from_state = line[0]
    to_state = line[3]
    if from_state not in states :
        G.add_node(from_state)
    if to_state not in states :
        G.add_node(to_state)
    G.add_edge(from_state, to_state)

circular_pos = nx.circular_layout(G)

# Drawing the graph with spring layout
plt.figure(figsize=(100, 100))  # Ensuring the figure size is square
self_loops = [(u, v) for u, v in G.edges() if u == v]
regular_edges = [(u, v) for u, v in G.edges() if u != v]

ax = plt.gca()
ax.set_aspect('equal', adjustable='box')

nx.draw_networkx_nodes(G, circular_pos, node_color='skyblue', node_size=1500)
nx.draw_networkx_labels(G, circular_pos, font_size=12)

# Drawing regular edges
nx.draw_networkx_edges(G, circular_pos, edgelist=regular_edges, 
                       arrowstyle='->', arrowsize=14, edge_color='black')

# Drawing self-loops with outward arcs
for loop_edge in self_loops:
    nx.draw_networkx_edges(G, circular_pos, edgelist=[loop_edge], 
                           arrowstyle='->', arrowsize=14, edge_color='black',
                           connectionstyle=f'arc3,rad=2')

plt.title("Pushdown Automata with Circular Layout and Outward Self-Loops")
plt.axis('off')
plt.show()