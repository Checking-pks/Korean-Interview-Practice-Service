import pandas as pd

def returnHtml(scoreList):
  question = pd.read_csv('면접 답안.csv')
  advice = pd.read_csv('면접 조언.csv')

  score = {}
  averageScore = 0
  averageRank = ''

  for s in scoreList:
    replyScore = s['gradingResult']['replyScore']
    
    for key, value in s['gradingResult'].items():
      if key == 'replyScore':
        continue
      if key in score.keys():
        score[key][0] += replyScore * value
        score[key][1] += value
      else:
        score[key] = [replyScore * value, value]
  
  for key in score.keys():
    score[key][0] /= score[key][1]
    averageScore += score[key][0]

  averageScore /= len(score)
  averageScore = round(averageScore)

  if averageScore == 100:
    averageRank = 'S+'
  elif averageScore >= 90:
    averageRank = 'S'
  elif averageScore >= 80:
    averageRank = 'A+'
  elif averageScore >= 70:
    averageRank = 'A'
  elif averageScore >= 60:
    averageRank = 'B+'
  elif averageScore >= 50:
    averageRank = 'B'
  elif averageScore >= 40:
    averageRank = 'C+'
  elif averageScore >= 30:
    averageRank = 'C'
  elif averageScore >= 20:
    averageRank = 'D+'
  elif averageScore >= 10:
    averageRank = 'D'
  else:
    averageRank = 'F'

  result = """
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
            <ul class="u-nav u-unstyled">
              <li class="u-nav-item"><button class="u-button-style u-nav-link">Main</button></li>
              <li class="u-nav-item"><button class="u-button-style u-nav-link">Test</button></li>
              <li class="u-nav-item"><button class="u-button-style u-nav-link">About</button></li>
            </ul>
          </div>
          <div class="u-custom-menu u-nav-container-collapse">
            <div class="u-black u-container-style u-inner-container-layout u-opacity u-opacity-95 u-sidenav">
              <div class="u-inner-container-layout u-sidenav-overflow">
                <div class="u-menu-close"></div>
                <ul class="u-align-center u-nav u-popupmenu-items u-unstyled u-nav-2">
                  <li class="u-nav-item"><button class="u-button-style u-nav-link">Main</button></li>
                  <li class="u-nav-item"><button class="u-button-style u-nav-link">Test</button></li>
                  <li class="u-nav-item"><button class="u-button-style u-nav-link">About</button></li>
                </ul>
              </div>
            </div>
            <div class="u-black u-menu-overlay u-opacity u-opacity-70"></div>
          </div>
        </nav>
      </div></header>
    <section class="u-clearfix u-palette-1-base u-section-1" id="carousel_2df3">
      <div class="u-clearfix u-sheet u-sheet-1">
        <div class="u-align-left u-container-style u-expanded-width-xs u-group u-palette-1-light-3 u-radius-10 u-shape-round u-group-1" style="margin-top: 20px;">
          <div class="u-container-layout u-valign-middle-lg u-valign-middle-md u-valign-middle-sm u-valign-middle-xl u-container-layout-1">
            <h2 class="u-text u-text-default u-text-1 u-text-palette-1-light-1">Test Result</h2>
            <p class="u-text u-text-default-lg u-text-default-xl u-text-2">모의 면접 결과 화면입니다.</p>
            <div class="u-expanded-width u-list u-list-1">
              <div class="u-repeater u-repeater-2">
                <div class="u-border-0 u-border-palette-1-base u-list u-list-flex-row u-list-item u-radius-24 u-white u-list-item-1">
                  <div id="gauge" style="height: 100%"></div>
                  <div class="u-table u-container-layout u-container-layout-2 u-product">
                    <div class="u-table u-container-layout u-container-layout-2 u-margin-top-bottom-auto">
                      <div class="u-text u-text-4 u-text-default u-text-palette-1-dark-2">당신의 면접 능력은</div>
                      <div class="u-text u-text-default u-text-3 u-text-palette-1-dark-2 u-text-align-center">""" + averageRank + "(" + str(averageScore) + """점)</div>
                      <div class="u-text u-text-4 u-text-default u-text-palette-1-dark-2 u-margin-left-auto-right-10px">입니다.</div></div>
                  </div>
                </div>
              </div>
            </div>
            <div class="u-expanded-width u-list u-list-1">
              <div class="u-repeater u-repeater-2">
                <div class="u-border-0 u-border-palette-1-base u-list u-list-flex-row u-list-item u-radius-24 u-white u-list-item-1 ">
                  <div id="radar" style="height: 100%"></div>
                  <div class="u-table u-container-layout u-container-layout-2">
                    <table class="u-table u-text u-text-default">
                      <tbody>"""

  for key in score.keys():
    if key == 'replyScore':
      continue

    result += """
                        <tr>
                          <td class="u-text u-text-table-question u-align-center">""" + key + """</td>
                          <td class="u-text u-text-table-score-1">""" + str(int(score[key][0])) + """</td>
                          <td class="u-text u-text-table-score-2">/ 100</td>
                        </tr>"""

  result += """
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
            <div class="u-expanded-width u-list u-list-2">
              <div class="u-repeater u-repeater-2">
                <div class="u-align-left u-border-12 u-border-palette-1-base u-container-style u-custom-item u-list-item u-radius-24 u-shape-round u-white u-list-item-2">"""

  for key in score.keys():
    result += """
                  <div class="u-container-layout u-similar-container u-container-layout-2">
                    <div class="u-text u-text-result-number">- """ + key + """</div>
                    <pre class="u-text u-text-result-reply">""" + advice[key][0] + """</pre>
                  </div>"""
  
  result += """
                </div>
              </div>
            </div>
            <div class="u-expanded-width u-list u-list-2">
              <div class="u-repeater u-repeater-2">
                <div class="u-align-left u-border-12 u-border-palette-1-base u-container-style u-custom-item u-list-item u-radius-24 u-shape-round u-white u-list-item-2">"""

  for i in range(len(scoreList)):
    result += """
                  <div class="u-container-layout u-similar-container u-container-layout-2">
                    <div class="u-text u-text-result-number">- """ + str(i + 1) + """번 문항</div>
                    <div class="u-text u-text-result-number"># QnA</div>
                    <pre class="u-text u-text-result-reply"> Q. """ + scoreList[i]['originQuestion'][1] + """</pre>
                    <pre class="u-text u-text-result-reply">""" + scoreList[i]['replyAnswer'] + """</pre>
                    <div class="u-text u-text-result-number"># 질문 의도</div>
                    <pre class="u-text u-text-result-reply">""" + question['질문 의도'][scoreList[i]['originQuestion'][0]] + """</pre>
                    <div class="u-text u-text-result-number"># 답변 포인트</div>
                    <pre class="u-text u-text-result-reply">""" + question['답변 포인트'][scoreList[i]['originQuestion'][0]] + """</pre>
                  </div>"""
  
  result += """
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <footer class="u-align-center u-clearfix u-footer u-grey-80 u-footer" id="sec-0fc3">
      <div class="u-clearfix u-sheet u-sheet-1">
        <p class="u-small-text u-text u-text-variant u-text-1">Made by DeepSummary</p>
      </div>
    </footer>
</body>"""

  return result