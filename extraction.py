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
    for i in range(len(odata)):
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
    for i in range(len(odata)):
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


def mine(filename):
    fe=file("explicit.txt","w+")
    fi=file("implicit.txt","w+")
    sent=sent_tokenize(file(filename).read())
    for i in range(0,len(sent)):
        sen=0
        file("temp.txt","w+").write(sent[i])
        result=str(extractor.execute("temp.txt",False))
        conj=extractor.findconj(result)
        if len(conj)==0:
            root=extractor.findroot(result)
            #sen=extractor.findsen(str(extractor.execute("temp.txt",False)),root)
            feat_word=extractor.findfeature(result,root)
            if len(feat_word)!=0:
                st=0
                boost=extractor.findboost(result,root)
                if len(boost)>0:
                    pos,neg=strength.get(boost+" "+root)
                else:
                    pos,neg=strength.get(root)
                if pos>(0-neg):
                    st=pos
                else:
                    st=neg
                if extractor.findneg(result)==1:
                                     st=0-st
                state=str(sent[i]).split('\n')
                fe.write(str(state[0])+"=["+str(feat_word)+"] ["+str(root)+"]:"+str(st)+"\n")
                print state[0],"=[",feat_word,"] [",root,"]"
                database(feat_word,root)
            else:
                st=0
                if len(boost)>0:
                    pos,neg=strength.get(boost+" "+root)
                else:
                    pos,neg=strength.get(root)
                if pos>(0-neg):
                    st=pos
                else:
                    st=neg
                if extractor.findneg(result)==1:
                                     st=0-st
                state=str(sent[i]).split('\n')
                feat_word=feature(root)
                fi.write(str(state[0])+"=["+str(feat_word)+"] ["+str(root)+"]:"+str(st)+"\n")
                print state[0],"= [",feat_word,"] [",root,"]"
                database(feat_word,root)
        else:
            temp=str(sent).split(conj)
            for j in range(len(temp)):
                sen=0
                file("temp.txt","w+").write(temp[j])
                result=str(extractor.execute("temp.txt",False))
                root=extractor.findroot(result)
                #sen=extractor.findsen(str(extractor.execute("temp.txt",False)),root)
                feat_word=extractor.findfeature(result,root)
                if sen==0:
                    fe.write(sent[i]+"= ["+feat_word+"] ["+root+"]\n")
                    print sent[i],"= [",feat_word,"] [",root,"]"
                    database(feat_word,root)
                else:
                    feat_word=feature(root)
                    fi.write(sent[i]+"= ["+feat_word+"] ["+root+"]\n")
                    print sent[i],"= [",feat_word,"] [",root,"]"
                    database(feat_word,root)
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


