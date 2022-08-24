import pandas as pd

question = pd.read_csv('면접 답안.csv')

def makeTableStr():
  resultStr = ""

  for q, a in zip(question['질문 문항'], question['답변 포인트']):
    resultStr += """
    <tr>
    <td>""" + q + """
    </td>
    <td>""" + a + """
    </td>
    </tr>"""

  return resultStr

def returnHtml():
    return """
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
      </div></header> 
      <section class="u-clearfix u-palette-1-base u-section-1" id="carousel_b93f">
      <div class="u-clearfix u-sheet u-sheet-1">
        <div class="u-align-left u-container-style u-expanded-width-xs u-group u-palette-1-light-3 u-radius-10 u-shape-round u-group-1" style="margin-top: 20px;">
          <div class="u-container-layout u-valign-middle-lg u-valign-middle-md u-valign-middle-sm u-valign-middle-xl u-container-layout-1">
            <h1 class="u-custom-font u-font-georgia u-text u-text-palette-1-light-1 u-text-1" style="margin-bottom: 20px;">QnA</h1><table>
    <tbody><tr><th>Question</th>
    <th>Answer</th></tr></tbody><tbody>""" + makeTableStr() + """
</tbody></table>
          </div>
        </div>
      </div>
    </section>
    <footer class="u-align-center u-clearfix u-footer u-grey-80 u-footer" id="sec-0fc3"><div class="u-clearfix u-sheet u-sheet-1">
        <p class="u-small-text u-text u-text-variant u-text-1">Made by DeepSummary</p>
      </div></footer>
</body></html>
    """