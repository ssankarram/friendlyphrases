from afinn import Afinn
import json
from pprint import pprint #not needed 
import urllib.request
import random

afinn = Afinn()
bad_phrase = input('Phrase: ').lower()
bad_phrase_list = bad_phrase.split(" ")
cursewords_in_phrase = {}
negative_words = []
links = {}
sorted_options = {}
final_list = {}

cursewords = json.load(open('cursewords.json'))
curseword_list = list(cursewords["Sheet1"].keys())
base_link = "http://words.bighugelabs.com/api/2/57fb326159dfcfd866e6778b33b451fb/"

def reset_link():
    base_link = "http://words.bighugelabs.com/api/2/57fb326159dfcfd866e6778b33b451fb/"

for i in range (len(bad_phrase_list)):
    word_score = afinn.score(bad_phrase_list[i])
    if word_score < 0:
        negative_words.append(bad_phrase_list[i])
  
for i in range (len(negative_words)):
    if negative_words[i] in curseword_list:
        cursewords_in_phrase[negative_words[i]] = cursewords["Sheet1"][negative_words[i]]["synonyms"].split(", ")
        continue
    else:
        base_link += (negative_words[i] + "/json")
        req = urllib.request.Request(base_link)
        r = urllib.request.urlopen(req).read()
        dict = json.loads(r.decode('utf-8'))
        if negative_words[i] not in links:
            links[negative_words[i]] = dict
        base_link = "http://words.bighugelabs.com/api/2/57fb326159dfcfd866e6778b33b451fb/"

for key in cursewords_in_phrase:
    links[key] = cursewords_in_phrase[key]

print("Rather, try the following: ")
afinn_score = 0

synonyms = {}
final_good_sentences = {}

#implement this whole part with google nl api instead of try/except blocks
for i in range(5):
    bad_phrase_good = bad_phrase
    for key in negative_words:
        if key in curseword_list:
            len_ = len(cursewords_in_phrase[key])
            synonyms[key] = cursewords_in_phrase[key][random.randint(0, len_-1)]
        else:
            word = "adjective"
            try:
                len_ = len(links[key]["adjective"]['syn'])
            except:
                try:
                    word = "verb"
                    len_ = len(links[key][word]['syn'])
                except:
                    word = "noun"
                    len_ = len(links[key][word]['syn'])
                
            synonyms[key] = links[key][word]['syn'][random.randint(0,len_-1)]
    for key in synonyms:
        bad_phrase_good = bad_phrase_good.replace(key, synonyms[key])
    afinn_score = afinn.score(bad_phrase_good)
    final_good_sentences[afinn_score] = bad_phrase_good
    afinn_score = 0

sorted_final_keys = sorted(final_good_sentences.keys())
for afinn_key in sorted_final_keys[::-1]:
    if afinn_key > afinn.score(bad_phrase):
        final_list[afinn_key] = final_good_sentences[afinn_key]

for key in final_list:
    percentage = (int(key) + 50) + (int(key) * 10)
    print(str(percentage) + '% positive : ' + str(final_list[key]))

fout = "answers.txt"
fo = open(fout, "w")

fo.write('let text = `')
fo.write("{")
for k, v in final_list.items():
    fo.write("\'" + str(k) + "\'" + ': \'' + str(v) + '\'')
    fo.write('\n')
fo.write("}")
fo.write('`')
fo.close()