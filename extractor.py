from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.tag import untag
from nltk.corpus import stopwords
import os
import subprocess
import re


def execute(filename,verbose):
    cmd="java -mx150m -cp *; edu.stanford.nlp.parser.lexparser.LexicalizedParser  -outputFormat typedDependencies edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz "+filename
    p=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output=p.communicate()
    ret=p.poll()
    if ret:
        raise subprocess.CalledProcessError(ret,cmd,output=output[0])
    return output

def findconj(string):
    conj=""
    temp=list()
    temp1=list()
    new=string.replace('\\r\\n','*')
    temp=new.split('*')
    temp1=str(temp[3]).split('\\n')
    for i in range(len(temp1)-1):
        if 'conj' in temp1[i]:
            temp=str(temp1[i]).split('_')
            temp=str(temp[1]).split('(')
            conj=str(temp[0])
        elif 'mark' in temp1[i]:
            temp=str(temp1[i]).split(' ')
            temp=str(temp[1]).split('-')
            conj=str(temp[0])
    return conj


def findboost(string,root):
    boost=""
    temp=list()
    temp1=list()
    new=string.replace('\\r\\n','*')
    temp=new.split('*')
    temp1=str(temp[3]).split('\\n')
    for i in range(len(temp1)-1):
        if 'advmod' in str(temp1[i]) and root in str(temp1[i]):
            temp=str(temp1[i]).split(' ')
            if root in temp[0]:
                temp=str(temp[1]).split('-')
                boost=str(temp[0])
            else:
                temp=str(temp[0]).split('(')
                temp=str(temp[1]).split('-')
                boost=str(temp[0])
    return boost


def findneg(string):
    f=0
    adj=""
    temp=list()
    temp1=list()
    new=string.replace('\\r\\n','*')
    temp=new.split('*')
    temp1=str(temp[3]).split('\\n')
    for i in range(len(temp1)-1):
        if 'neg' in temp1[i]:
            f=1
    return f


def findfeature(string,root):
    positive=str(file("positive.txt").read().lower()).split('\n')
    negative=str(file("negative.txt").read().lower()).split('\n')
    feat_word=""
    temp=list()
    temp1=list()
    new=string.replace('\\r\\n','*')
    temp=new.split('*')
    temp1=str(temp[3]).split('\\n')
    for i in range(len(temp1)-1):
       if 'dobj' in temp1[i] and root in temp1[i]:
            temp=str(temp1[i]).split(' ')
            feat=str(temp[1]).split('-')
            if feat[0]!=root:
                feat_word=str(feat[0])
            else:
                temp=str(temp1[i]).split('(')
                feat=str(temp[1]).split('-')
                feat_word=str(feat[0])
            feat_tag=str(pos_tag(word_tokenize(feat_word)))
            if 'NN' in feat_tag or 'NNS' in feat_tag:
                return feat_word
            else:
                feat_word=""
    if len(feat_word)==0:
        for i in range(len(temp1)-1):
            if 'nsubj' in temp1[i] and root in temp1[i]:
                temp=str(temp1[i]).split(' ')
                feat=str(temp[1]).split('-')
                if feat[0]!=root:
                    feat_word=str(feat[0])
                else:
                    temp=str(temp1[i]).split('(')
                    feat=str(temp[1]).split('-')
                    feat_word=str(feat[0])
                feat_tag=str(pos_tag(word_tokenize(feat_word)))
                if 'NN' in feat_tag or 'NNS' in feat_tag:
                    break
                else:
                    feat_word=""
    if len(feat_word)==0:
        for i in range(len(temp1)-1):
            if 'acomp' in temp1[i] and root in temp1[i]:
                temp=str(temp1[i]).split(' ')
                feat=str(temp[1]).split('-')
                if feat[0]!=root:
                    feat_word=str(feat[0])
                else:
                    temp=str(temp1[i]).split('(')
                    feat=str(temp[1]).split('-')
                    feat_word=str(feat[0])
                feat_tag=str(pos_tag(word_tokenize(feat_word)))
                if 'NN' in feat_tag or 'NNS' in feat_tag:
                    return feat_word
                else:
                    feat_word=""
    if len(feat_word)>0:
        for i in range(len(temp1)-1):
            if 'nn' in temp1[i] and feat_word in temp1[i]:
                temp=str(temp1[i]).split(' ')
                feat=str(temp[1]).split('-')
                if feat[0]==feat_word:
                    temp=str(temp1[i]).split('(')
                    feat=str(temp[1]).split('-')
                t=str(pos_tag(word_tokenize(str(feat[0]))))
                if 'JJ' in t:
                    break
                else:
                    aflag=0
                    for j in range(len(positive)):
                        if str(feat[0])==str(positive[j]):
                            aflag=1
                            break
                    for j in range(len(negative)):
                        if str(feat[0])==str(negative[j]):
                            aflag=1
                            break
                    if aflag==0 and ('NN' in t or 'NNS' in t):
                        t=feat_word
                        feat_word=str(feat[0])+" "+t
                break
            elif 'amod' in str(temp1[i]) and feat_word in str(temp1[i]):
                temp=str(temp1[i]).split(' ')
                feat=str(temp[1]).split('-')
                if feat[0]==feat_word:
                    temp=str(temp1[i]).split('(')
                    feat=str(temp[1]).split('-')
                t=str(pos_tag(word_tokenize(str(feat[0]))))
                if 'JJ' in t:
                    break
                else:
                    aflag=0
                    for j in range(len(positive)):
                        if str(feat[0])==str(positive[j]):
                            aflag=1
                            break
                    for j in range(len(negative)):
                        if str(feat[0])==str(negative[j]):
                            aflag=1
                            break
                    if aflag==0 and ('NN' in t or 'NNS' in t):
                        t=feat_word
                        feat_word=str(feat[0])+" "+t
                break
    else:
        for i in range(len(temp1)-1):
            if 'amod' in temp1[i] and root in temp1[i]:
                temp=str(temp1[i]).split(' ')
                feat=str(temp[1]).split('-')
                if feat[0]==root:
                    temp=str(temp1[i]).split('(')
                    feat=str(temp[1]).split('-')
                feat_word=str(feat[0])
                feat_tag=str(pos_tag(word_tokenize(feat_word)))
                if 'NN' in feat_tag or 'NNS' in feat_tag:
                    return feat_word
                else:
                    feat_word=""
        if len(feat_word)>0:
            for i in range(len(temp1)-1):
                if 'nn' in temp1[i] and feat_word in temp1[i]:
                    temp=str(temp1[i]).split(' ')
                    feat=str(temp[1]).split('-')
                    if feat[0]==feat_word:
                        temp=str(temp1[i]).split('(')
                        feat=str(temp[1]).split('-')
                    t=str(pos_tag(word_tokenize(str(feat[0]))))
                    if 'JJ' in t:
                        break
                    else:
                        aflag=0
                        for j in range(len(positive)):
                            if str(feat[0])==str(positive[j]):
                                aflag=1
                                break
                        for j in range(len(negative)):
                            if str(feat[0])==str(negative[j]):
                                aflag=1
                                break
                        if aflag==0 and ('NN' in t or 'NNS' in t):
                            t=feat_word
                            feat_word=str(feat[0])+" "+t
                    break
                elif 'nsubj' in str(temp1[i]) and feat_word in str(temp1[i]):
                    temp=str(temp1[i]).split(' ')
                    feat=str(temp[1]).split('-')
                    if feat[0]==feat_word:
                        temp=str(temp1[i]).split('(')
                        feat=str(temp[1]).split('-')
                    t=str(pos_tag(word_tokenize(str(feat[0]))))
                    if 'JJ' in t:
                        break
                    else:
                        aflag=0
                        for j in range(len(positive)):
                            if str(feat[0])==str(positive[j]):
                                aflag=1
                                break
                        for j in range(len(negative)):
                            if str(feat[0])==str(negative[j]):
                                aflag=1
                                break
                        if aflag==0 and ('NN' in t or 'NNS' in t):
                            t=feat_word
                            feat_word=str(feat[0])+" "+t
                    break
        else:
            for i in range(len(temp1)-1):
                if 'nn' in temp1[i] and root in temp1[i]:
                    temp=str(temp1[i]).split(' ')
                    feat=str(temp[1]).split('-')
                    if feat[0]==root:
                        temp=str(temp1[i]).split('(')
                        feat=str(temp[1]).split('-')
                    feat_word=str(feat[0])
                    break
    return feat_word


def findroot(string):
    positive=str(file("positive.txt").read().lower()).split('\n')
    negative=str(file("negative.txt").read().lower()).split('\n')
    root_word=""
    temp=list()
    temp1=list()
    new=string.replace('\\r\\n','*')
    temp=new.split('*')
    temp1=str(temp[3]).split('\\n')
    for i in range(len(temp1)-1):
        if 'root' in str(temp1[i]):
            temp=str(temp1[i]).split(' ')
            root=str(temp[1]).split('-')
            root_word=str(root[0])
            break
    for j in range(len(temp1)-1):
        if 'acomp' in str(temp1[j]) and root_word in str(temp1[j]):
            temp=str(temp1[j]).split(' ')
            root=str(temp[1]).split('-')
            root_word=str(root[0])
            break
    root_tag=str(pos_tag(word_tokenize(root_word)))
    if 'pratik' in root_tag:
        return root_word
    else:
        aflag=0
        for j in range(len(positive)):
            if str(root_word)==str(positive[j]):
                aflag=1
                break
        for j in range(len(negative)):
            if str(root_word)==str(negative[j]):
                aflag=1
                break
        if aflag==0:
            troot=root_word
            root_word=""
            for j in range(len(temp1)-1):
                if 'dobj' in str(temp1[j]) and troot in str(temp1[j]):
                    temp=str(temp1[j]).split(' ')
                    root=str(temp[1]).split('-')
                    if troot!=root[0]:
                        root_word=str(root[0])
                    else:
                        temp=str(temp1[j]).split('(')
                        root=str(temp[1]).split('-')
                        root_word=str(root[0])
                    break
            aflag=0
            if len(root_word)!=0:
                for j in range(len(positive)):
                    if str(root_word)==str(positive[j]):
                        aflag=1
                        break
                for j in range(len(negative)):
                    if str(root_word)==str(negative[j]):
                        aflag=1
                        break
            if aflag==0:
                troot=root_word
                root_word=""
                for i in range(len(temp1)-1):
                    if 'amod' in temp1[i] and troot in temp1[i]:
                        temp=str(temp1[i]).split(' ')
                        root=str(temp[1]).split('-')
                        if root[0]!=troot:
                            root_word=str(root[0])
                        else:
                            temp=str(temp1[i]).split('(')
                            root=str(temp[1]).split('-')
                            root_word=str(root[0])
                        break
                root_tag=str(pos_tag(word_tokenize(root_word)))
                if 'JJ' in root_tag:
                    return root_word
                else:
                    if len(root_word)!=0:
                        aflag=0
                        for j in range(len(positive)):
                            if str(root_word)==str(positive[j]):
                                aflag=1
                                break
                        for j in range(len(negative)):
                            if str(root_word)==str(negative[j]):
                                aflag=1
                                break
                        if aflag==0:
                            root_word=""
                    if aflag==0:
                        for i in range(len(temp1)-1):
                            if 'nsubj' in temp1[i] and troot in temp1[i]:
                                temp=str(temp1[i]).split('(')
                                root=str(temp[1]).split('-')
                                if root[0]!=troot:
                                    root_word=str(root[0])
                                else:
                                    temp=str(temp1[i]).split(' ')
                                    root=str(temp[1]).split('-')
                                    root_word=str(root[0])
                                break
                        root_tag=str(pos_tag(word_tokenize(root_word)))
                        if 'JJ' in root_tag:
                            return root_word
                        else:
                            if len(root_word)!=0:
                                aflag=0
                                for j in range(len(positive)):
                                    if str(root_word)==str(positive[j]):
                                        aflag=1
                                        break
                                for j in range(len(negative)):
                                    if str(root_word)==str(negative[j]):
                                        aflag=1
                                        break
                                if aflag==0:
                                    root_word=""
    return root_word
            
def findsen(string,root):
    flag=0
    stops=list(stopwords.words('english'))
    new=string.replace('\\r\\n','*')
    temp=new.split('*')
    temp1=str(temp[3]).split('\\n')
    for i in range(len(temp1)-1):
        if 'nsubj' in str(temp1[i]) and root in str(temp1[i]):
            temp=str(temp1[i]).split(' ')
            feat=str(temp[1]).split('-')
            feat_word=str(feat[0])
            for j in range(len(stops)):
                if feat_word==str(stops[j]):
                    flag=1
                    break
            break
    if flag==0:
         for i in range(len(temp1)-1):
            if 'amod' in str(temp1[i]) and root in str(temp1[i]):
                temp=str(temp1[i]).split('(')
                temp=str(temp[1]).split('-')
                feat_word=str(temp[0])
                for j in range(len(stops)):
                    if feat_word==str(stops[j]):
                        flag=1
                        break
                break
    return flag
