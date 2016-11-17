import string
import random

authorlist = []
conferences = ["kdd", "icml", "vldb"]
connection = {}
sample = 0.2
random.seed()

authors = []
fileObj = open('../data/dblp.xml', 'r') 
for line in fileObj:
	if line.find('<author>') != -1:
		line = line.replace("<author>", "")
		line = line.replace("</author>", "")
		line = line.replace("\n", "")
		authors.append(line)
	if line.find('booktitle') != -1:
		line = line.replace("<booktitle>", "")
		line = line.replace("</booktitle>", "")
		line = line.replace("\n", "")
		line = line.lower()
		if conferences.count(line) > 0:
			for author in authors:
				if author not in authorlist:
					authorlist.append(author)

			for author_1 in authors:
				for author_2 in authors:
					if authorlist.index(author_1) != authorlist.index(author_2):
						connectionkey = str(authorlist.index(author_1))+","+str(authorlist.index(author_2))
						if connectionkey not in connection:
							connection[connectionkey] = {}
						if line not in connection[connectionkey]:
							connection[connectionkey][line] = 1
						else:
							connection[connectionkey][line] += 1

		authors = []

fileObj.close()

print(str(len(authorlist)))
fileObj = open('../data/authorlist.txt', 'w')
for author in authorlist:
	fileObj.write(author+"\n")
fileObj.close()


fileObjcon = open('../data/connection.txt' ,'w')
fileconfs = {}
for conf in conferences:
	fileconfs[conf] = open("../data/"+conf+".txt", "w")

for i in range(len(authorlist)):
	for j in range(len(authorlist)):
		connectionkey = str(i)+","+str(j)
		if (connectionkey in connection):
			fileObjcon.write(str(i)+" "+str(j)+"\n")
			for conf in conferences:
				if conf in connection[connectionkey]:
					if random.random() < sample:
						fileconfs[conf].write(str(i)+" "+str(j)+" "+str(connection[connectionkey][conf])+"\n")

fileObjcon.close()
for conf in conferences:
	fileconfs[conf].close()

