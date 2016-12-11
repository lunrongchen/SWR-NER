import math
import re
import numpy as np 
from scipy import spatial
dic = {}
path = 'glove.6B.50d.txt'
file = open(path)
pattern_key = r'[a-zA-Z\s]*'
pattern_num = r'[-0-9.]*'
count = 0

for row in file:
	words = row.split(' ')
	count = count + 1

	numbers = []
	key = ''
	for word in words:
		word = word.replace('\n','')
		eng  = re.search(pattern_key,word)
		eng = eng.group()
		num = re.search(pattern_num,word)
		num = num.group()
		if eng != '':
			key = eng
		if num != '':
			try:
				numbers.append(float(num))
			except:
				continue
	dic[key] = numbers

dicc = {}
path = 'glove.6B.50d.txt'
file = open(path)
count = 0
for row in file:
	words = row.split(' ')
	count = count + 1

	numbers = []
	key = ''
	for word in words:
		word = word.replace('\n','')
		eng  = re.search(pattern_key,word)
		eng = eng.group()
		num = re.search(pattern_num,word)
		num = num.group()
		if eng != '':
			key = eng
		if num != '':
			try:
				numbers.append(float(num))
			except:
				continue
	dicc[key] = numbers

distance = 0
for keys in dicc:
	if dic.has_key(keys):
		dist = 1 - spatial.distance.cosine(dicc[keys],dic[keys])
		distance = distance + dist
print distance