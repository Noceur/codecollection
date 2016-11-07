import networkx as nx
from natsort import natsorted
import itertools
import matplotlib.pyplot as plot

class MasterTemplate:

	# Data
	path 			= []
	pos				= []
	nodes 			= []
	edges 			= []
	layout 			= ""
	g 				= ""

	# Init
	def __init__(self, g):
		self.g = nx.Graph()

	# Class functions
	def add_nodes(self, nodes):
		for n in self.nodes:
			self.g.add_node(n)

	def add_edges(self, edges):
		for e in self.edges:
			self.g.add_edge(e[0], e[1])

	def show_plot(self, layout="spectral"):
		if self.layout == "spectral":
			self.pos = nx.spectral_layout(self.g)
		elif self.layout == "circular":
			self.pos = nx.circular_layout(self.g)
		elif self.layout == "random":
			self.pos = nx.random_layout(self.g)
		elif self.layout == "spring":
			self.pos = nx.spring_layout(self.g)
		elif self.layout == "shell":
			self.pos = nx.shell_layout(self.g)
		elif self.layout == "graphviz":
			self.pos = nx.graphviz_layout(self.g)

		print (self.nodes, self.edges, self.layout)

		nx.draw_networkx_nodes(self.g, self.pos)
		nx.draw_networkx_labels(self.g, self.pos)
		nx.draw_networkx_edges(self.g, self.pos)
		plot.axis("off")
		plot.show()












graphtest = MasterTemplate("test")

nodes = ["A", "B", "C", "D", "c1", "c2", "c3", "c4"]

edges = [
	("A", "c1"),
	("B", "c2"),
	("C", "c3"),
	("D", "c4"),
	("c1", "c2"),
	("c2", "c3"),
	("c3", "c4"),
	("c4", "c1")
]

graphtest.add_nodes(nodes)
graphtest.add_edges(edges)

graphtest.show_plot()