import matplotlib.pyplot as plt
import numpy as np
import math

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

fuse = 2
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
				for x in range(-fuse, fuse+1):
					for y in range (-fuse, fuse+1):
						if (authorlist.index(words[0])+x >= 0) and (authorlist.index(words[0])+x < n):
							if (authorlist.index(words[1])+y >= 0) and (authorlist.index(words[1])+y < n):
								#if float(words[2]) > 0:
								table[authorlist.index(words[0])+x][authorlist.index(words[1])+y] = math.log(float(words[2])+1)
	plt.clf()
	plt.imshow(table, cmap='hot', interpolation='lanczos')
	plt.savefig("../figures/holistic/" + conf + "heat.png")
	#plt.show()

for conf in confs:
	table = []
	n = len(authorlist)
	for i in range(n):
		table += [[0] * n]

	f = "../results/single/" + conf + "all.txt"
	with open(f) as input_:
		input_.readline()
		while 1:
			line = input_.readline()
			if not line:
				break
			words = line.split(",")
			if authorlist.count(words[0]) > 0 and authorlist.count(words[1]) > 0:
				for x in range(-fuse, fuse+1):
					for y in range (-fuse, fuse+1):
						if (authorlist.index(words[0])+x >= 0) and (authorlist.index(words[0])+x < n):
							if (authorlist.index(words[1])+y >= 0) and (authorlist.index(words[1])+y < n):
								#if float(words[2]) > 0:
								table[authorlist.index(words[0])+x][authorlist.index(words[1])+y] = math.log(float(words[2])+1)
	plt.clf()
	plt.imshow(table, cmap='hot', interpolation='lanczos')
	plt.savefig("../figures/single/" + conf + "heat.png")
	#plt.show()

