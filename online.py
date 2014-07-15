import urllib
import sys
import re
 
def get(feature):
    synonym=[]
    antonym=[]
    url = 'http://thesaurus.com/browse/' + feature +'?posfilter=adjective'
    temp=urllib.urlopen(url).readlines()
    for i in range(400,600):
        if 'synonym-description' in str(temp[i]):
            break
    for j in range(i,2000):
        if '<span class="text">' in str(temp[j]):
            word=str(temp[j]).split('">')
            word=str(word[1]).split('<')
            synonym.append(word[0])
        if 'synonyms-horizontal-divider' in str(temp[j]):
            break
    for i in range(j,3000):
        if '<span class="text">' in str(temp[i]):
            word=str(temp[i]).split('">')
            word=str(word[1]).split('<')
            antonym.append(word[0])
        if '21st Century Thesaurus' in str(temp[i]):
            break
    return synonym,antonym


