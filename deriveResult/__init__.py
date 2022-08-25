from . import RNN
from . import findKeyword
from . import compareKeywords

def score(str):
    return RNN.totalscore(str)

def keyword(str):
    return findKeyword.find_keyword(str)

def drawRedColor(str):
    return RNN.drawColor(str)

def drawBlueColor(str):
    return compareKeywords.find_goodsentence(str)