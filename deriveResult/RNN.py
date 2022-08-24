# -*- coding: utf-8 -*-
import re
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import pickle

with open('deriveResult/data.pickle','rb') as f:
    tokenizer = pickle.load(f)

okt = Okt() #한글 형태소 분류 정의
stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다'] #불용어 정의
#tokenizer = Tokenizer()
#tokenizer.fit_on_texts(X_train)
max_len = 30
loaded_model = load_model('deriveResult/best_model_1.h5')

def sentiment_predict(x):
    new_sentence = x
    
    new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', new_sentence)
    new_sentence = okt.morphs(new_sentence, stem=True) # 토큰화
    new_sentence = [word for word in new_sentence if not word in stopwords] # 불용어 제거
    encoded = tokenizer.texts_to_sequences([new_sentence]) # 정수 인코딩
    pad_new = pad_sequences(encoded, maxlen = max_len) # 패딩
    
    try:
        score = float(loaded_model.predict(pad_new)) # 예측
        return score
    except:
        return 0.51

def textcolor(x):
    return x if sentiment_predict(x) > 0.5 else ('<span style="color:coral">'+ x+'</span>')

def drawColor(x):
    predict_list=[]
    splittext=x.split('.')
    for i in splittext:
        predict_list.append(textcolor(i))
    result='. '.join(predict_list)
    return result

def totalscore(x):
    splitText = x.split('.')

    totalscore=0

    for i in splitText:
        totalscore += float(sentiment_predict(i))

    listlen = len(splitText)

    resultScore = totalscore/listlen

    return resultScore * 100

#x='감각과 행동에서 이해해 가는 성격입니다.진짜짜증나네.학과공부도 열심히 했지만 그에 못지 않게 동아리 활동도 열심히 했습니다.어린 아이들을 돌보는 동아리였습니다.제가 그 아이들에게 도움이 주었다기 보다는 늘 제가 더 큰 교훈을 얻고 돌아오곤 했습니다.'
