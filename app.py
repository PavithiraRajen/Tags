import json
from flask import Flask
from flask import request
from flask import jsonify
import re
import os
# from keybert import KeyBERT
import yake
app = Flask(__name__)
@app.route('/tag-api-1',methods=['GET','POST'])
def endpoint2():
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
  max_ngram_size = 3
  deduplication_threshold = 0.1
  numOfKeywords = 3
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

# def preprocess(c):
#     clean = re.compile('<.*?>')
#     return re.sub(clean, '', c)
    

    
# def yake_kw(i):
#     i = preprocess(i)
#     kw_extractor = yake.KeywordExtractor()
#     language = "en"
#     max_ngram_size = 3
#     deduplication_threshold = 0.1
#     numOfKeywords = 3
#     custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None, stopwords=None) 
#     keywords = custom_kw_extractor.extract_keywords(i)
#     yake_key = []
#     for kw, v in keywords:
#       #print("Keyphrase: ",kw, ": score", v)
#       yake_key.append(kw.title())
#     return yake_key
# ################# 

# @app.route('/tag-api-2', methods=['GET','POST'])
# def index():
#   req = request.get_json()
#   list1 = []
#   list1.append({'html':req['article-content']})
#   i = ', '.join(strings['html'] for strings in list1)
#   print(i)
#   print(type(i))
#   print("Preprocess works")
#   kw_model = KeyBERT(model="all-MiniLM-L6-v2")
#   clean = re.compile('<.*?>')
#   re.sub(clean, '', i)
#   language = "english"
#   max_ngram_size = (1, 3)
#   numOfKeywords = 3
#   keywords = kw_model.extract_keywords(i,keyphrase_ngram_range= max_ngram_size,stop_words= language,top_n= numOfKeywords, diversity=0.2)
#   keywords_list= list(dict(keywords).keys())
#   final_keywords_list = [i.title() for i in keywords_list]
#   d1 = dict(enumerate(final_keywords_list))
#   y = json.dumps(d1)
#   return y

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000,debug=True)
