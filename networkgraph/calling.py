import classtest

graphtest = MasterTemplate("test")

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
