from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
import operator

extractor = ConllExtractor()


def train(Q):
    keyPhrases = {}
    data_set = Q.data_set
    for ans in data_set:
        blob = TextBlob(ans, np_extractor=extractor)
        phrases = list(blob.noun_phrases)
        for phrase in phrases:
            if phrase in keyPhrases:
                keyPhrases[phrase] +=1
            else:
                keyPhrases[phrase] = 1
    sorted_phrases = sorted(keyPhrases.items(), key=operator.itemgetter(1),reverse=True)
    Q.setPhrases(keyPhrases)
    

def evaluate(Q,ans):
    marks = Q.marks
    keyPhrases = Q.phrases
    if marks == 2:
        nKeyPhrases =  2
    if marks == 3:
        nKeyPhrases =  4
    if marks == 4:
        nKeyPhrases =  5
    if marks == 5:
        nKeyPhrases =  8
    if marks == 10:
        nKeyPhrases =  15
    if len(keyPhrases.keys()) < nKeyPhrases:
        nKeyPhrases = len(keyPhrases.keys())
    ansMarks = 0
    blob = TextBlob(ans, np_extractor=extractor)
    phrases = list(set(blob.noun_phrases))

    for phrase in phrases:
        if phrase in keyPhrases:
            ansMarks = ansMarks+ (marks/nKeyPhrases)
        if ansMarks == marks:
            break
 
    return ansMarks
 


"""
{'full cognizance': 1, 'broad range': 1, 'more specific emphasis': 1, 'empirical evidence': 1, 'engineering': 1, 'creative application': 2}
{'president': 1, 'india': 4, 'republic day honours': 1, 'new delhi': 1, 'main republic day celebration': 1, 'india act': 1, 'government': 1, 'constitution': 1, 'rajpath': 2, 'national capital': 1, 'rich cultural heritage': 1, '26 january 1950': 1}
"""