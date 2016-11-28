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


B-company
B-facility
B-geo-loc
B-movie
B-musicartist
B-other
B-person
B-product
B-sportsteam
B-tvshow
I-company
I-facility
I-geo-loc
I-movie
I-musicartist
I-other
I-person
I-product
I-sportsteam
I-tvshow
O
