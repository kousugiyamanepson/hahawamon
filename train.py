import gensim
from gensim.models import word2vec
import os

path =  './models'
sentences = word2vec.LineSentence("wakachi.txt")
os.makedirs(path)
print("学習中")
model = word2vec.Word2Vec(sentences,
                          sg=1,
                          size=100,
                          min_count=1,
                          window=13,
                          hs=1,
                          negative=0)
print("保存中")
model.save(path+'/learn.model')
print("完了")

