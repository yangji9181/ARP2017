import matplotlib.pyplot as plt
import numpy as np



confs = ["kdd", "icml", "vldb"]
pairlist = []
for conf in confs:
	f = "../results/holistic/" + conf + "all.txt"
	ls = []
	with open(f) as input_:
		input_.readline()
		while 1:
			line = input_.readline()
			if not line:
				break
			words = line.split(",")
			if (float(words[2]) > 0):
				ls.append(words[0]+","+words[1])
	pairlist.append(ls)

table = []
n = len(pairlist)
for i in range(n):
	table += [[0] * n]
for i in range (len(pairlist)):
	for j in range(len(pairlist)):
		if i != j:
			for pair1 in pairlist[i]:
				if pairlist[j].count(pair1) > 0:
					table[i][j] += 1
print table

plt.clf()
plt.imshow(table, cmap='Blues', interpolation='nearest')
plt.savefig("../figures/vxvheat.png")
#plt.show()


