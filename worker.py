from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
import operator

extractor = ConllExtractor()


def train(Q):
    keyPhrases = {}
    data_set = Q.data_set
    for ans in data_set:
        blob = TextBlob(ans, np_extractor=extractor)
        phrases = list(set(blob.noun_phrases))
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
    nKeyPhrases =  len(keyPhrases)
    ansMarks = 0
    blob = TextBlob(ans, np_extractor=extractor)
    phrases = list(set(blob.noun_phrases))

    for phrase in phrases:
        if phrase in keyPhrases:
            ansMarks = ansMarks+ (marks/nKeyPhrases)
 
    return ansMarks
 
