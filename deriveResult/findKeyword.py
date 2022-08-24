import numpy as np
import itertools

from konlpy.tag import Okt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

def find_keyword(doc):
    okt = Okt()
    
    n_gram_range = (2, 3)
    top_n = 5

    tokenized_doc = okt.pos(doc)
    tokenized_nouns = ' '.join([word[0] for word in tokenized_doc if word[1] == 'Noun'])
    count = CountVectorizer(ngram_range=n_gram_range).fit([tokenized_nouns])
    candidates = count.get_feature_names()
    model = SentenceTransformer('sentence-transformers/xlm-r-100langs-bert-base-nli-stsb-mean-tokens')
    doc_embedding = model.encode([doc])
    candidate_embeddings = model.encode(candidates)
    distances = cosine_similarity(doc_embedding, candidate_embeddings)
    keywords = [candidates[index] for index in distances.argsort()[0][-top_n:]]
    
    return keywords