import word2vec
import sys

def getWordVector(_fileName):
    phraseName = _fileName + "-phrases.txt"
    binName = _fileName + ".bin"
    outPutName = _fileName + "_100d.vocab"
    file  = open(outPutName, 'wt')
    word2vec.word2phrase(_fileName, phraseName, verbose=True)
    word2vec.word2vec(phraseName, binName, size=100, verbose=True)
    model = word2vec.load(binName)
    for key in model.vocab:
        vectorLine = key
        for value in model[key]:
            vectorLine = vectorLine + " " + str(value)
        file.write(vectorLine + "\n")
    file.close()

# fileName = "RSV1Subset"
# for d in xrange(0,10):
#     fileNameText = fileName + str(d) + ".txt"
#     getWordVector(fileNameText)
getWordVector("RCV1testTagOutput.txt")
