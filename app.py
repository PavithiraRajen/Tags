import json
from flask import Flask
from flask import request
from flask import jsonify
import re
import os
# from keybert import KeyBERT
import yake
app = Flask(__name__)
@app.route('/tag',methods=['GET','POST'])
def tag():
  req = request.get_json()
  list1 = []
  list1.append({'html':req['article-content']})
  i = ', '.join(strings['html'] for strings in list1)
  print(i)
  print(type(i))
  print("Preprocess works")
  clean = re.compile('<.*?>')
  re.sub(clean, '', i)
  kw_extractor = yake.KeywordExtractor()
  language = "en"
  max_ngram_size = 4
  deduplication_threshold = 0.1
  numOfKeywords = 5
  custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None, stopwords=None) 
  keywords = custom_kw_extractor.extract_keywords(i)
  yake_key = []
  for kw, v in keywords:
    #print("Keyphrase: ",kw, ": score", v)
    yake_key.append(kw.title())
  d1 = {}
  d1['Tags'] = yake_key
  #d1 = dict(enumerate(yake_key))
  #y = json.dumps(d1)
  return d1


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run()
