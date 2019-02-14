from data_set import new_data as data
from rake_nltk import Rake, Metric
import pickle
r = Rake()

r.extract_keywords_from_text(data)
keywords = r.get_ranked_phrases()

f = open("o.json","wb")
pickle.dump(keywords,f)
print(keywords)
