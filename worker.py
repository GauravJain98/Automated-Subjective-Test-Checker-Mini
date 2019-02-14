import operator
from rake_nltk import Rake, Metric

def train(Q):
    keyPhrases = []
    data_set = Q.data_set
    r = Rake()
    r.extract_keywords_from_text(data_set['train_ans'])
    keywords = r.get_ranked_phrases()
    Q.setPhrases(keywords)

def evaluate(Q,ans):
    marks = Q.marks
    keyPhrases = Q.phrases
    ans , testmarks = ans

    ansMarks = 0.0
    r = Rake()
    r.extract_keywords_from_text(ans)
    phrases = r.get_ranked_phrases()
    for phrase in phrases:
        if phrase in keyPhrases:
            ansMarks = ansMarks+ .2
        if ansMarks == marks:
            break
 
    return ansMarks,testmarks
 


"""
{'full cognizance': 1, 'broad range': 1, 'more specific emphasis': 1, 'empirical evidence': 1, 'engineering': 1, 'creative application': 2}
{'president': 1, 'india': 4, 'republic day honours': 1, 'new delhi': 1, 'main republic day celebration': 1, 'india act': 1, 'government': 1, 'constitution': 1, 'rajpath': 2, 'national capital': 1, 'rich cultural heritage': 1, '26 january 1950': 1}
"""