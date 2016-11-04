import networkx as nx
from natsort import natsorted
import itertools
import matplotlib.pyplot as plot

connections = [
	("A", 1),
	("B", 2),
	("C", 3),
	("D", 4),
	("c1", 1),
	("c1", 5),
	("c1", 8),
	("c2", 2),
	("c2", 5),
	("c2", 6),
	("c3", 3),
	("c3", 6),
	("c3", 7),
	("c4", 4),
	("c4", 7),
	("c4", 8)
]

connection2 = [
	("A", 1),
	("B", 2),
	("C", 3),
	("D", 4),
	("c1", 1),
	("c1", 5),
	("c1", 8),
	("c2", 2),
	("c2", 5),
	("c2", 6),
	("c3", 3),
	("c3", 6),
	("c3", 7),
	("c4", 4),
	("c4", 7),
	("c4", 8)
]

nodes = ["A", "B", "C", "D", "c1", "c2", "c3", "c4"]

G=nx.Graph()

for n in nodes:
	G.add_node(n)

G.add_edge("A", "c1")
G.add_edge("B", "c2")
G.add_edge("C", "c3")
G.add_edge("D", "c4")
G.add_edge("c1", "c2")
G.add_edge("c2", "c3")
G.add_edge("c3", "c4")
G.add_edge("c4", "c1")


#for c in connections:
#	G.add_edge(c[0], c[1])

# draw your graph

pos = nx.spectral_layout(G)

nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
#nx.draw_networkx_edge_labels(G, pos)

'''colors=[]
for i in G.nodes_iter():
   colors+=[G.degree(i)]
for i in range(0,n):
   colors[i]/=max(colors)

nx.draw_spectral(G,node_color=colors,width=1.5,with_labels=False,alpha=.5,node_size=50,cmap=pylab.cm.Blues,edge_color='w')
fig.set_facecolor("#000000")'''

#nx.draw(G)
plot.axis("off")
plot.show()