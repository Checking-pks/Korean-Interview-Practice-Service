# streamlit
import streamlit as st
from streamlit_multipage import MultiPage

questionNum = 0

def saveAnswer(reply):
  print(reply)
  MultiPage.save({reply.key: reply})

def htmlHeader():
  st.markdown(
    """
<body class="u-body u-xl-mode u-responsive-xl"><header class="u-clearfix u-header u-header" id="sec-d9ff"><div class="u-clearfix u-sheet u-sheet-1">
        <button data-page-id="459313545" class="u-image u-logo u-image-1" data-image-width="412" data-image-height="74" title="Main">
          <img src="https://i.ibb.co/87prwNb/Kakao-Talk-20220709-135034667.png" class="u-logo-image u-logo-image-1">
        </button>
        <nav class="u-menu u-menu-dropdown u-offcanvas u-menu-1">
          <div class="menu-collapse">
            <button class="u-button-style u-nav-link">
              <svg class="u-svg-link" viewBox="0 0 24 24"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#svg-1038"></use></svg>
              <svg class="u-svg-content" version="1.1" id="svg-1038" viewBox="0 0 16 16" x="0px" y="0px" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg"><g><rect y="1" width="16" height="2"></rect><rect y="7" width="16" height="2"></rect><rect y="13" width="16" height="2"></rect>
</g></svg>
            </button>
          </div>
          <div class="u-custom-menu u-nav-container">
            <ul class="u-nav u-unstyled"><li class="u-nav-item"><button class="u-button-style u-nav-link">Main</button>
</li><li class="u-nav-item"><button class="u-button-style u-nav-link">Test</button>
</li><li class="u-nav-item"><button class="u-button-style u-nav-link">About</button>
</li></ul>
          </div>
          <div class="u-custom-menu u-nav-container-collapse">
            <div class="u-black u-container-style u-inner-container-layout u-opacity u-opacity-95 u-sidenav">
              <div class="u-inner-container-layout u-sidenav-overflow">
                <div class="u-menu-close"></div>
                <ul class="u-align-center u-nav u-popupmenu-items u-unstyled u-nav-2"><li class="u-nav-item"><button class="u-button-style u-nav-link">Main</button>
</li><li class="u-nav-item"><button class="u-button-style u-nav-link">Test</button>
</li><li class="u-nav-item"><button class="u-button-style u-nav-link">About</button>
</li></ul>
              </div>
            </div>
            <div class="u-black u-menu-overlay u-opacity u-opacity-70"></div>
          </div>
        </nav>
      </div></header>""",
      unsafe_allow_html=True
  )

def htmlFooter():
  st.markdown("""
      <section class="u-clearfix u-section-6" id="sec-1e7c">
      <div class="u-clearfix u-sheet u-sheet-1">
        <button data-page-id="29297956" class="u-btn u-button-style u-hover-palette-1-dark-1 u-palette-1-base u-btn-2" style="left: calc(50% - 313.47px / 2);">Result</button>
      </div>
    </section>
    <footer class="u-align-center u-clearfix u-footer u-grey-80 u-footer" id="sec-0fc3"><div class="u-clearfix u-sheet u-sheet-1">
        <p class="u-small-text u-text u-text-variant u-text-1">Made by DeepSummary</p>
      </div></footer>
</body>""",
    unsafe_allow_html=True
  )

def resetQuestion():
  global questionNum
  questionNum = 0

def addQuestion(question):
  global questionNum
  questionNum += 1

  if questionNum == 1:
    st.markdown("""
  <section class="u-align-center u-clearfix u-palette-1-base u-section-1" id="sec-d5cf">
      <div class="u-clearfix u-sheet u-sheet-1">
      <img class="u-image u-image-contain u-image-default u-image-1" src="https://i.ibb.co/FhGs2Nn/min.png" alt="" data-image-width="1245" data-image-height="707">
          <h2 class="u-text u-text-default u-text-1">Question 1</h2>
        <p class="u-text u-text-default u-text-2">질문을 보고 질문에 대한 답을 작성해주세요</p>
        <div class="u-expanded-width u-list u-list-1">
          <div class="u-repeater u-repeater-1">
            <div class="u-align-left u-border-12 u-border-palette-3-base u-container-style u-custom-item u-list-item u-radius-24 u-repeater-item u-shape-round u-white u-list-item-1">
              <div class="u-container-layout u-similar-container u-container-layout-1">
                <p class="u-text u-text-default u-text-3">""" + question + """</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>""",
      unsafe_allow_html=True
    )
  else:
    st.markdown("""
  <section class="u-align-center u-clearfix u-palette-1-base u-section-1" id="sec-d5cf">
      <div class="u-clearfix u-sheet u-sheet-1">
          <h2 class="u-text u-text-default u-text-1">Question """ + str(questionNum) + """</h2>
        <p class="u-text u-text-default u-text-2">질문을 보고 질문에 대한 답을 작성해주세요</p>
        <div class="u-expanded-width u-list u-list-1">
          <div class="u-repeater u-repeater-1">
            <div class="u-align-left u-border-12 u-border-palette-3-base u-container-style u-custom-item u-list-item u-radius-24 u-repeater-item u-shape-round u-white u-list-item-1">
              <div class="u-container-layout u-similar-container u-container-layout-1">
                <p class="u-text u-text-default u-text-3">""" + question + """</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>""",
      unsafe_allow_html=True
    )

  st.text_area(
    label="Answer", 
    key="reply" + str(questionNum),
    placeholder="질문을 보고 답변을 작성해주세요"
  )

def infoReply(num):
  try:
    return st.session_state['reply' + str(num)]
  except:
    return ''

    