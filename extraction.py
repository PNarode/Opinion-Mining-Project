"""
This Programme Divides the Input file into sentences then check whether any adjective is present or not.
If the adjective is found then it is check if it is positive or negative.
On the basis of that the sentence is classified as Negative of Positive.
"""

from nltk.tag import pos_tag
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import re
import extractor
import online
import strength



def database(feat,root):
    ip=file("database.txt","r+")
    odata=(ip.read()).split("\n")
    ndata=[]
    flag=0
    for i in range(len(odata)-1):
        temp=str(odata[i]).split('=')
        if (feat in str(temp[0]) or str(temp[0]) in feat) and (len(temp[0])>1):
            feat=str(temp[0])
            flag=1
        else:
            ndata.append(str(odata[i])+"\n")
    ndata.insert(0,feat+"="+root+"\n")
    ip=file("database.txt","w+")
    for i in range(len(ndata)):
        ip.write(str(ndata[i]))
    return


def feature(root):
    ip=file("database.txt","r+")
    odata=(ip.read()).split("\n")
    rsynonym,rantonym=online.get(root)
    for i in range(len(odata)-1):
        temp=str(odata[i]).split('=')
        tsynonym,tantonym=online.get(temp[1])
        for j in range(len(rsynonym)):
            for k in range(len(tsynonym)):
                if str(rsynonym[j])==str(tsynonym[k]):
                    return temp[0]
            for k in range(len(tantonym)):
                if str(rsynonym[j])==str(tantonym[k]):
                    return temp[0]
        for j in range(len(rantonym)):
            temp=str(odata[i]).split('=')
            tsynonym,tantonym=online.get(temp[1])
            for k in range(len(tsynonym)):
                if str(rantonym[j])==str(tsynonym[k]):
                    return temp[0]
            for k in range(len(tantonym)):
                if str(rantonym[j])==str(tantonym[k]):
                    return temp[0]
    return


def collocation():
    sent=str(file("explicit.txt").read()).split('\n')
    for i in range(len(sent)-1):
        temp=str(sent[i]).split('[')
        temp1=str(temp[1]).split(']')
        feat=str(temp1[0])
        root=str(temp[2]).split(']')
        if len(root)>1:
            root=str(root[0]).split('-')
            if len(str(root[len(root)-1]))>1:
                database(str(feat),str(root[len(root)-1]))
            else:
                database(str(feat),str(root[len(root)-2]))
    return


def implicit(filename):
    collocation()
    sent=str(file(filename).read()).split('\n')
    fi=file(filename,"w+")
    for i in range(len(sent)-1):
        temp=str(sent[i]).split('=')
        temp1=str(temp[1]).split('-')
        if len(temp1[len(temp1)-1])>1:
            feat_word=feature(str(temp1[len(temp1)-1]))
            fi.write(str(temp[0])+"=["+str(feat_word)+"] ["+str(temp[1])+"]")
            database(str(feat_word),str(temp1[len(temp1)-1]))
    return


def mine(filename):
    fe=file("explicit.txt","w+")
    fi=file("implicit.txt","w+")
    sent=sent_tokenize(file(filename).read())
    i=0
    
    while i!=len(sent):
        file("temp.txt","w+").write(sent[i])
        result=str(extractor.execute("temp.txt",False))
        conj=extractor.findconj(result)
        if len(conj)==0:
            root=extractor.findroot(result)
            feat_word=extractor.findfeature(result,root)
            boost=extractor.findboost(result,root)
            if len(feat_word)>1:
                state=str(sent[i]).split('\n')
                if len(boost)>1:
                    if len(root)>1:
                        fe.write(str(state[0])+"=["+str(feat_word)+"] ["+str(boost)+"-"+str(root)+"]\n")
                    else:
                        fe.write(str(state[0])+"=["+str(feat_word)+"] ["+str(boost)+"]\n")
                else:
                    fe.write(str(state[0])+"=["+str(feat_word)+"] ["+str(root)+"]\n")
            else:
                state=str(sent[i]).split('\n')
                if len(root)>1:
                    if len(boost)>1:
                        if len(root)>1:
                            fi.write(str(state[0])+"="+str(boost)+"-"+str(root)+"\n")
                        else:
                            fi.write(str(state[0])+"="+str(boost)+"\n")
                    else:
                        fi.write(str(state[0])+"="+str(root)+"\n")
            i=i+1
        else:
            if conj=="and":
                temp=str(sent[i]).split(conj)
                if len(temp)==1:
                    temp=str(sent[i]).split('&')
            else:
                temp=str(sent[i]).split(conj)
            file("temp.txt","w+").write(temp[1])
            result=str(extractor.execute("temp.txt",False))
            root=extractor.findroot(result)
            feat_word=extractor.findfeature(result,root)
            boost=extractor.findboost(result,root)
            if len(feat_word)>1:
                if len(boost)>1:
                    if len(root)>1:
                        fe.write(str(state[0])+"=["+str(feat_word)+"] ["+str(boost)+"-"+str(root)+"]\n")
                    else:
                        fe.write(str(state[0])+"=["+str(feat_word)+"] ["+str(boost)+"]\n")
                else:
                    fe.write(str(temp[1])+"=["+str(feat_word)+"] ["+str(root)+"]\n")
            else:
                state=str(sent[i]).split('\n')
                if len(root)>1:
                    if len(boost)>1:
                        if len(root)>1:
                            fi.write(str(state[0])+"="+str(boost)+"-"+str(root)+"\n")
                        else:
                            fi.write(str(state[0])+"="+str(boost)+"\n")
                    else:
                        fi.write(str(state[0])+"="+str(root)+"\n")
            sent[i]=temp[0]
    return


def classify(filename):
    sent=sent_tokenize(file(filename).read())
    fc=file("comments.txt","w+")
    ff=file("facts.txt","w+")
    for i in range(0,len(sent)):
        file("temp.txt","w+").write(sent[i])
        root=extractor.findroot(str(extractor.execute("temp.txt",False)))
        if len(root)==0:
            ff.write(sent[i]+"\n")
        else:
            fc.write(sent[i]+"\n")
    return


def check():
    try:
        f=file("explicit.txt")
        f.close()
    except:
        f=file("explicit.txt","w+")
        f.close()
    try:
        f=file("implicit.txt")
        f.close()
    except:
        f=file("implicit.txt","w+")
        f.close()
    return


