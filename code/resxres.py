import matplotlib.pyplot as plt
import numpy as np



confs = ["kdd", "icml", "vldb"]
authorlist = []
for conf in confs:
	f = "../results/holistic/" + conf + "top.txt"
	with open(f) as input_:
		input_.readline()
		while 1:
			line = input_.readline()
			if not line:
				break
			words = line.split(",")
			if authorlist.count(words[0]) == 0:
				authorlist.append(words[0])
			if authorlist.count(words[1]) == 0:
				authorlist.append(words[1])


for conf in confs:
	table = []
	n = len(authorlist)
	for i in range(n):
		table += [[0] * n]

	f = "../results/holistic/" + conf + "all.txt"
	with open(f) as input_:
		input_.readline()
		while 1:
			line = input_.readline()
			if not line:
				break
			words = line.split(",")
			if authorlist.count(words[0]) > 0 and authorlist.count(words[1]) > 0:
				table[authorlist.index(words[0])][authorlist.index(words[1])] = float(words[2])
	plt.clf()
	plt.imshow(table, cmap='hot', interpolation='nearest')
	plt.savefig("../figures/" + conf + "heat.png")
	plt.show()

