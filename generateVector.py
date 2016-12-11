
# import ipy_autoreload
# load_ext autoreload
# autoreload 2

import word2vec
import sys

# filename = "text8"
# phraseName = filename + "-phrases.txt"
# binName = filename + ".bin"
# outPutName = filename + "_100d.vocab"

# file  = open(outPutName, 'wt')

# word2vec.word2phrase('text8', 'text8-phrases', verbose=True)

# word2vec.word2vec('text8-phrases', 'text8.bin', size=100, verbose=True)

# model = word2vec.load('text8.bin')

    

def getWordVector(_fileName):
    phraseName = _fileName + "-phrases.txt"
    binName = _fileName + ".bin"
    outPutName = _fileName + "_100d.vocab"
    file  = open(outPutName, 'wt')
    word2vec.word2phrase(_fileName, phraseName, verbose=True)
    word2vec.word2vec(phraseName, binName, size=100, verbose=True)
    model = word2vec.load(binName)
    unknownLine = "UNKNOWN"
    paddingLine = "PADDING"
    for value in model['unknown']:
        unknownLine = unknownLine + " " + str(value)
        paddingLine = paddingLine + " " + str(value)
    file.write(unknownLine + "\n")
    file.write(paddingLine + "\n")
    for key in model.vocab:
        vectorLine = key
        for value in model[key]:
            vectorLine = vectorLine + " " + str(value)
        file.write(vectorLine + "\n")
    file.close()

getWordVector("text8")