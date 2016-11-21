#Requirement:
conda create --name=tensorflow_env python=2.7

source activate tensorflow_env

pip install unidecode

pip install Theano

pip install keras==1.0.0

source deactivate


#Command:
python CreateWordList.py

python CreateSubCorpus.py vocabulary.txt embeddings/GermEval.vocab

python NER_with_Caseing.py