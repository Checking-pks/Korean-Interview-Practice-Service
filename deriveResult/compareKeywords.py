import pickle
import numpy as np
import itertools

from konlpy.tag import Okt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer


#모범답안 키워드 리스트 로드
def load_keywordslist():
    with open("deriveResult/list.pickle","rb") as f:
        keywordlist = pickle.load(f)
    return keywordlist

#키워드 리스트와 문장 비교 문장마다 키워드가 절반 이상 있을 시 글씨색을 파란색으로 반환
def comparekeyword(sentence, keywordlist):
    score = 0
    sentence_keyword=find_keyword(sentence) #문장의 키워드 추출
    for i in keywordlist:
        if i in sentence_keyword:
            score += 1
    return sentence+'.' if score < (len(sentence_keyword)/2) else ('<span style="color:blue">'+sentence+'. </span>')   

#input= 문단
#사용시 글자 색상 적용 후 다시 string으로 반환
def find_goodsentence(x):
    keywordlist=load_keywordslist()
    sentence_list=[]
    splittext=x.split('.')
    splittext = [v for v in splittext if v] #공백 제거
    for i in splittext:
        sentence_list.append(comparekeyword(i,keywordlist))
    result=''.join(sentence_list)
    return result

def find_keyword(doc):
    okt = Okt()

    tokenized_doc = okt.pos(doc)
    tokenized_nouns = ' '.join([word[0] for word in tokenized_doc if word[1] == 'Noun'])
    n_gram_range = (1, 1)
    count = CountVectorizer(ngram_range=n_gram_range).fit([tokenized_nouns])
    candidates = count.get_feature_names()
    model = SentenceTransformer('sentence-transformers/xlm-r-100langs-bert-base-nli-stsb-mean-tokens')
    doc_embedding = model.encode([doc])
    candidate_embeddings = model.encode(candidates)
    top_n = 10
    distances = cosine_similarity(doc_embedding, candidate_embeddings)
    keywords = [candidates[index] for index in distances.argsort()[0][-top_n:]]
    return keywords