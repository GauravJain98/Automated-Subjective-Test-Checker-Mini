import operator
from rake_nltk import Rake, Metric
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from data_set import *
from nltk.stem import WordNetLemmatizer
import string
def keywordGenerator(train):
    r = Rake()
    lemma=WordNetLemmatizer()
    r.extract_keywords_from_text(train)
    keywords = r.get_ranked_phrases()
    finalkeywords = []
    for keys in keywords:
        keys=word_tokenize(keys)
        puncs = ["‘",".","’"] + string.punctuation.split()
        stopwords = ["(",")"]
        resultwords  = [word for word in puncs if word.lower() not in stopwords]
        keys = [i for i in keys if i not in resultwords]
        stemmed = []
        for words in keys:
            stemmed.append(lemma.lemmatize(words))
        finalkeywords.append(" ".join(stemmed))
    return finalkeywords

def train(Q):
    keyPhrases = []
    data_set = Q.data_set
    Q.setPhrases(keywordGenerator(data_set["train_ans"]))

def evaluate(Q):
    marks = Q.marks
    keyPhrases = Q.phrases
    for text,marks in Q.data_set["test"]:
        ansMarks = 0.0
        phrases=keywordGenerator(text)
        for phrase in phrases:
            if phrase in keyPhrases:
                ansMarks = ansMarks+ (Q.marks/len(Q.phrases))
        print(ansMarks,marks)
 


"""
{'full cognizance': 1, 'broad range': 1, 'more specific emphasis': 1, 'empirical evidence': 1, 'engineering': 1, 'creative application': 2}
{'president': 1, 'india': 4, 'republic day honours': 1, 'new delhi': 1, 'main republic day celebration': 1, 'india act': 1, 'government': 1, 'constitution': 1, 'rajpath': 2, 'national capital': 1, 'rich cultural heritage': 1, '26 january 1950': 1}
"""