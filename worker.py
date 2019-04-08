import operator
from rake_nltk import Rake, Metric
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from data_set import *
from nltk.stem import WordNetLemmatizer
import string
import math

Table = {}


def keywordGenerator(train):
    r = Rake()
    ansLen = len(train)
    lemma = WordNetLemmatizer()
    avgWordDict = {}
    keyword = []
    allStemmed = {}
    wordDict = {}
    r.extract_keywords_from_text(train)
    keywords = r.get_ranked_phrases()
    finalkeywords = []
    for keys in keywords:
        keys = word_tokenize(keys)
        puncs = ["‘", ".", "’"] + string.punctuation.split()
        #stopwords = ["(", ")"]
        # resultwords = [word.lower()
        #              for word in puncs if word.lower() not in stopwords]
        keys = [i for i in keys if i not in puncs]
        stemmed = []
        for words in keys:
            stemmed.append(lemma.lemmatize(words))
        #finalkeywords.append(" ".join(stemmed))
        # print(stemmed)
        for stem in stemmed:
            if stem in allStemmed:
                allStemmed[stem] += 1/ansLen
            else:
                allStemmed[stem] = 1/ansLen
    return allStemmed


def train():
    keywordTf = {}
    noOfDocs = len(final_dataset[0]['data']['train_ans'])
    for train_ans in final_dataset[0]['data']["train_ans"]:
        keywordDict = keywordGenerator(train_ans)
        for key in keywordDict.keys():
            if key in keywordTf:
                keywordTf[key] += 1/keywordDict[key]
            else:
                keywordTf[key] = 1/keywordDict[key]
    return keywordTf


def computeTF():
    global Train
    Train = train()
    noOfDocs = len(final_dataset[0]['data']['train_ans'])
    allWts = 0
    for train_ans in final_dataset[0]['data']["train_ans"]:
        ansWt = 0
        keywordDict = keywordGenerator(train_ans)
        for key in keywordDict.keys():
            if key in Train:
                ansWt += Train[key]
        allWts += ansWt/noOfDocs
    final_dataset[0]['data']['fullWt'] = allWts
    return allWts


computeTF()


def evaluate(ans):
    global Train
    allWts = final_dataset[0]['data']['fullWt']
    maxMarks = final_dataset[0]['max_marks']
    ansWt = 0
    keywordDict = keywordGenerator(ans)
    for key in keywordDict.keys():
        if ansWt >= allWts:
            break
        if key in Train:
            ansWt += Train[key]
    return ansWt*maxMarks/allWts
    # marks = Q.marks
    # keyPhPasess = Q.phrases
    # mse = 0
    # for text, marks in final_dataset[0]['data']["test"]:
    #     ansMarks = 0.0
    #     phrases = keywordGenerator(text)
    #     for phrase in phrases:
    #         if phrase in keyPhPasess:
    #             ansMarks = ansMarks + (Q.marks/len(Q.phrases))
    #     print(ansMarks, marks)
    #     add = pow(((ansMarks-marks)/marks), 2)
    #     print(add)
    #     mse = mse + add
    # print((pow(mse, 0.5)))
