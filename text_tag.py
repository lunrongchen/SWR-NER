import nltk
import re
from nltk.tokenize import sent_tokenize

path = 'output.txt'
final_ans = []
file = open(path)

count = 0
for row in file:
	try:
		# row = row.decode('Cp1252','ignore')
		sentence = sent_tokenize(row)
		for everyline in sentence:
			word = nltk.word_tokenize(everyline)
			pos_tags = nltk.pos_tag(word)
			count = count + 1
			final_ans.extend(pos_tags)

		if count > 1000:
			break
	except Exception,e:
		continue

ans = []

for everyitem in final_ans:
	ans.append(everyitem[0])
	ans.append(everyitem[1])

string = ''

for item in ans:
	string = string + ' ' + item

path = 'Combine.txt'
file = open(path,'w')
for item in string:
	file.write("%s" % item)


