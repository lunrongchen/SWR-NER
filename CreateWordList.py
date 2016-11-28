"""
Reads in our files and outputs all words to a vocabulary file

@author: Nils Reimers
"""

filenames = ['new_data/NER-de-test.tsv', 'new_data/NER-de-dev.tsv', 'new_data/NER-de-train.tsv']
outputfile = 'dictionary.txt'

words = set()

for filename in filenames:
    for line in open(filename): 
        line = line.strip()
        
        if len(line) == 0 or line[0] == '#':
            continue
        
        splits = line.split('\t')
        
        words.add(splits[1])
    
fOut = open(outputfile, 'w')    
for word in sorted(words):
    fOut.write(word+'\n')
    
print "Done, words exported"