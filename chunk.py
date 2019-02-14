import nltk
from data_set import new_data as data
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
import operator

extractor = ConllExtractor()
phrase = [] 
sent=nltk.sent_tokenize(data)
for text in sent:
    blob = TextBlob(text, np_extractor=extractor)
    phrase = phrase + list(blob.noun_phrases)

print(set(phrase))
