import pylab
import networkx as nx

#Set up a sample graph
n=100
G=nx.barabasi_albert_graph(n, 3, seed=None)
#Generate a color sequence for the nodes based on degree
colors=[]
for i in G.nodes_iter():
   colors+=[G.degree(i)]
for i in range(0,n):
   colors[i]/=max(colors)


#Create figure; attempt to set background to light gray
fig = pylab.figure()
ax = fig.add_subplot(111)
nx.draw_spectral(G,node_color=colors,width=1.5,with_labels=False,alpha=.5,node_size=50,cmap=pylab.cm.Blues,edge_color='w')
fig.set_facecolor("#000000")
pylab.show()

