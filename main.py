# streamlit
import streamlit as st
import streamlit.components.v1 as components
from streamlit_pages.streamlit_pages import MultiPage

import random
import pandas as pd

import loadWebsite
import deriveResult

questionNumber = 5

questions = pd.read_csv('면접 답안.csv')

def home():
    loadWebsite.resetQuestion()

    randNumList = []
    ran_num = random.randint(0, len(questions)-1)

    for i in range(questionNumber):
        while ran_num in randNumList:
            ran_num = random.randint(0, len(questions)-1)
        randNumList.append(ran_num)

    for i in randNumList:
        loadWebsite.addQuestion(i, questions['질문 문항'][i])

    loadWebsite.loadHomePage()

def test():
    loadWebsite.loadTestPage()

def about():
    loadWebsite.loadAboutPage()

def result():
    loadWebsite.resetScoreList()

    for i in range(questionNumber):
        replyScore = deriveResult.score(st.session_state['reply' + str(i+1)])
        replyIdx = loadWebsite.infoQuestion(i, 'idx')

        loadWebsite.addScore({
            'originQuestion':   [replyIdx, loadWebsite.infoQuestion(i, 'str')],
            'replyAnswer':      deriveResult.drawColor(st.session_state['reply' + str(i+1)]),
            
            'gradingResult': {
                'replyScore': replyScore,
                '자기 표현력': questions['자기 표현력'][replyIdx],
                '리더십 역량': questions['리더십 역량'][replyIdx],
                '직무 역량':   questions['직무 역량'][replyIdx],
                '태도 역량':   questions['태도 역량'][replyIdx],
                '인간 관계':   questions['인간 관계'][replyIdx]
            }
        })

    loadWebsite.loadResultPage()

app = MultiPage()

app.add_page("Home", home)
app.add_page("Test", test)
app.add_page("About", about)
app.add_page("Result", result)

app.run()
