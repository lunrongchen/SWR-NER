import numpy as np
path = "glove.6B/glove.6B.50d.txt"
path_ = "glove.6B/glove.6B.100d.txt"
file = open(path)
file_ = open(path_)

dic = {}
count = 0
for row in file:
	row = row.split(' ')
	if not dic.has_key(row[0]):
		num = []
		for item in row[1:101]:
			nu = float(item)
			num.append(nu)
		dic[row[0]] = num
	
dic_ = {}
count = 0
finalresult = []
for row in file_:
	row = row.split(' ')
	if  dic.has_key(row[0]):
		# print dic[row[0]]
		# print row[1:100]
		sub = []
		sub.extend(dic[row[0]])
		num = []
		for item in row[1:101]:
			nu = float(item)
			num.append(nu)
		sub.extend(num)
		dic[row[0]] = sub
		item = []
		item.append(row[0])
		item.extend(dic[row[0]])
		finalresult.append(item)

file = open('glove_50+100.txt','w')
for item in finalresult:
	count = 0
	for word in item:
		count = count + 1
		file.write("%s " % word)
		if count == 201:
			file.write("\n")

	
		




