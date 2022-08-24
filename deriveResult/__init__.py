import deriveResult.RNN as RNN
import deriveResult.findKeyword as findKeyword

def score(str):
    return RNN.totalscore(str)

def keyword(str):
    return findKeyword.find_keyword(str)

def drawColor(str):
    return RNN.drawColor(str)