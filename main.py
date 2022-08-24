# streamlit
import streamlit as st
from streamlit_multipage import MultiPage

import random
import pandas as pd

import loadWebsite
import deriveResult

questionNumber = 5

questions = pd.read_csv('면접 답안.csv')

def home(st, **state):
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

def test(st, **state):
    loadWebsite.loadTestPage()

def about(st, **state):
    loadWebsite.loadAboutPage()

def result(st, **state):
    loadWebsite.resetScoreList()

    for i in range(questionNumber):
        replyScore = deriveResult.score(loadWebsite.infoReply(i+1))
        replyIdx = loadWebsite.infoQuestion(i, 'idx')

        loadWebsite.addScore({
            'originQuestion':   [replyIdx, loadWebsite.infoQuestion(i, 'str')],
            'replyAnswer':      deriveResult.drawColor(loadWebsite.infoReply(i+1)),
            
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
app.st = st

app.add_app("Result", result)
app.add_app("About", about)
app.add_app("Test", test)
app.add_app("Home", home)

app.run()
