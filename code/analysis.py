import string

conferences = ["kdd", "icml", "vldb"]
top = 1000
alpha = 0.9




for conf in conferences:
	connections = []
	weights = []
	feac = []
	feaf = []
	fileObj = open('../data/connection.txt', 'r')
	for line in fileObj:
		words = line.split()
		if (len(words) == 2):
			author_1 = int(words[0])
			while len(connections) - 1 < author_1:
				connections.append([])
				weights.append([])
			connections[author_1].append(int(words[1]))
			weights[author_1].append(0)
	fileObj.close()

	fileObj = open("../data/"+conf+'.txt', 'r')
	for line in fileObj:
		words = line.split()
		if (len(words) == 3):
			author_1 = int(words[0])
			while len(feac) - 1 < author_1:
				feac.append([])
				feaf.append([])
			feac[author_1].append(int(words[1]))
			feaf[author_1].append(int(words[2]))
			weights[author_1][connections[author_1].index(int(words[1]))] = int(words[2])
	fileObj.close()

	fileObj = open('../data/authorlist.txt', 'r')
	authorlist = []
	for line in fileObj:
		authorlist.append(line.strip())
	fileObj.close()

	highlist_value = []
	highlist_a1 = []
	highlist_a2 = []
	for i in range(len(connections)):
		for j in connections[i]:
			if len(highlist_value) < top:
				highlist_value.append(weights[i][connections[i].index(j)])
				highlist_a1.append(i)
				highlist_a2.append(j)
			else:
				ind = highlist_value.index(min(highlist_value))
				if (weights[i][connections[i].index(j)] > min(highlist_value)):
					highlist_value[ind] = weights[i][connections[i].index(j)]
					highlist_a1[ind] = i
					highlist_a2[ind] = j

	for i in range(len(highlist_value)-1):
		maxvalue = 0
		p = 0
		for j in range(i, len(highlist_value)):
			if highlist_value[j] > maxvalue:
				maxvalue = highlist_value[j]
				p = j
		temp = highlist_value[i]
		highlist_value[i] = highlist_value[p]
		highlist_value[p] = temp
		temp = highlist_a1[i]
		highlist_a1[i] = highlist_a1[p]
		highlist_a1[p] = temp
		temp = highlist_a2[i]
		highlist_a2[i] = highlist_a2[p]
		highlist_a2[p] = temp

	fileObj = open("../results/single/"+conf+'top.txt', 'w')
	maxvalue = highlist_value[0]
	fileObj.write(str(maxvalue)+"\n")
	for i in range(top):
		fileObj.write(authorlist[highlist_a1[i]]+","+authorlist[highlist_a2[i]]+","+str(highlist_value[i]*1.0/maxvalue)+"\n")

	fileObj.close()

	fileObj = open("../results/single/"+conf+'all.txt', 'w')
	for i in range(len(connections)):
		for j in connections[i]:
			fileObj.write(authorlist[i]+","+authorlist[j]+","+str(weights[i][connections[i].index(j)]*1.0/maxvalue)+"\n")
	fileObj.close()

	length2 = {}
	for i in range(len(feac)):
		for j in feac[i]:
			tot = 0
			key = str(i)+","+str(j)
			for k in connections[i]:
				if j in connections[k]:
					tot += 1
					if (key not in length2):
						length2[key] = []
					length2[key].append(k)
			if tot > 0:
				for k in length2[key]:
					weights[i][connections[i].index(k)] += alpha*feaf[i][feac[i].index(j)]/tot
					weights[k][connections[k].index(j)] += alpha*feaf[i][feac[i].index(j)]/tot

	length3 = {}
	for i in range(len(feac)):
		for j in feac[i]:
			bigkey = str(i)+","+str(j)
			tot = 0
			for k in connections[i]:
				key = str(k)+","+str(j)
				if key in length2:
					if (bigkey not in length3):
						length3[bigkey] = []
					length3[bigkey].append(k)
					for p in length2[key]:
						tot += 1
			if tot > 0:
				for k in length3[bigkey]:
					key = str(k)+","+str(j)
					for p in length2[key]:
						weights[i][connections[i].index(k)] += alpha*alpha*feaf[i][feac[i].index(j)]/tot
						weights[k][connections[k].index(p)] += alpha*alpha*feaf[i][feac[i].index(j)]/tot
						weights[p][connections[p].index(j)] += alpha*alpha*feaf[i][feac[i].index(j)]/tot

	

	fileObj = open('../data/authorlist.txt', 'r')
	authorlist = []
	for line in fileObj:
		authorlist.append(line.strip())
	fileObj.close()

	highlist_value = []
	highlist_a1 = []
	highlist_a2 = []
	for i in range(len(connections)):
		for j in connections[i]:
			if len(highlist_value) < top:
				highlist_value.append(weights[i][connections[i].index(j)])
				highlist_a1.append(i)
				highlist_a2.append(j)
			else:
				ind = highlist_value.index(min(highlist_value))
				if (weights[i][connections[i].index(j)] > min(highlist_value)):
					highlist_value[ind] = weights[i][connections[i].index(j)]
					highlist_a1[ind] = i
					highlist_a2[ind] = j

	for i in range(len(highlist_value)-1):
		maxvalue = 0
		p = 0
		for j in range(i, len(highlist_value)):
			if highlist_value[j] > maxvalue:
				maxvalue = highlist_value[j]
				p = j
		temp = highlist_value[i]
		highlist_value[i] = highlist_value[p]
		highlist_value[p] = temp
		temp = highlist_a1[i]
		highlist_a1[i] = highlist_a1[p]
		highlist_a1[p] = temp
		temp = highlist_a2[i]
		highlist_a2[i] = highlist_a2[p]
		highlist_a2[p] = temp

	fileObj = open("../results/holistic/"+conf+'top.txt', 'w')
	maxvalue = highlist_value[0]
	fileObj.write(str(maxvalue)+"\n")
	for i in range(top):
		fileObj.write(authorlist[highlist_a1[i]]+","+authorlist[highlist_a2[i]]+","+str(highlist_value[i]*1.0/maxvalue)+"\n")

	fileObj.close()

	fileObj = open("../results/holistic/"+conf+'all.txt', 'w')
	for i in range(len(connections)):
		for j in connections[i]:
			fileObj.write(authorlist[i]+","+authorlist[j]+","+str(weights[i][connections[i].index(j)]*1.0/maxvalue)+"\n")
	fileObj.close()

