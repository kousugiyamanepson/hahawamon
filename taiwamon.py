import MeCab
import sys
import re
from gensim.models import word2vec

model = word2vec.Word2Vec.load('models/learn.model')

print("文章を入力してください")
data = input()

mecab = MeCab.Tagger()
parse = mecab.parse(data)
lines = parse.split('\n')
items = (re.split('[\t,]', line) for line in lines)



words = [item[0]
         for item in items
         if (item[0] not in ('EOS', '', 't', 'ー') and
             item[1] == '名詞' and item[2] == '一般')]
newdoc = data
count = 0
for i in words:
    change = model.most_similar(str(i),[],1)[0][0]
    print(model.most_similar(str(i),[],1)[0][0])
    newdoc = newdoc.replace(str(i), change)
#    newdoc += "\n"
    count += 1
print(newdoc)
