from nltk.tokenize import sent_tokenize
import online
import strength
import extractor


def scoring():
    sent=str(file("explicit.txt").read()).split('\n')
    fe=file("explicit.txt","w+")
    for i in range(len(sent)-1):
        temp=str(sent[i]).split('=')
        temp1=str(temp[1]).split('[')
        temp1=str(temp1[len(temp1)-1]).split(']')
        root=str(temp1[0])
        file("temp.txt","w+").write(temp[1])
        result=str(extractor.execute("temp.txt",False))
        st=0
        pos,neg=strength.get(root)
        if pos>(0-neg):
            st=pos
        else:
            st=neg
        if extractor.findneg(result)==1:
            st=0-st
        fe.write(str(sent[i])+":"+str(st)+"\n")
    sent=str(file("implicit.txt").read()).split('\n')
    fi=file("implicit.txt","w+")
    for i in range(len(sent)-1):
        temp=str(sent[i]).split('=')
        temp1=str(temp[1]).split('[')
        temp1=str(temp1[len(temp1)-1]).split(']')
        root=str(temp1[0])
        file("temp.txt","w+").write(temp[1])
        result=str(extractor.execute("temp.txt",False))
        st=0
        pos,neg=strength.get(root)
        if pos>(0-neg):
            st=pos
        else:
            st=neg
        if extractor.findneg(result)==1:
            st=0-st
        fi.write(str(sent[i])+":"+str(st)+"\n")
    return


def rank(exp,imp):
    scoring()
    check()
    explicit=str(file(exp,"r").read()).split('\n')
    for i in range(len(explicit)-1):
        flag=0
        temp=str(explicit[i]).split('[')
        feat=str(str(temp[1]).split(']')[0])
        temp=(str(temp[2]).split(':'))[1]
        value=int(temp)
        data=file('ranked.txt','r').read().split('\n')
        rk=file('ranked.txt','w')
        for j in range(len(data)-1):
            temp=str(data[j]).split('=')
            if feat==str(temp[0]) or feat in str(temp[0]) or str(temp[0]) in feat:
                flag=1
                temp[1]=value+int(temp[1])
                temp[2]=int(temp[2])+4
                if value>0:
                    temp[3]=int(temp[3])+1
                else:
                    temp[4]=int(temp[4])+1
            rk.write(str(temp[0])+'='+str(temp[1])+'='+str(temp[2])+'='+str(temp[3])+'='+str(temp[4])+'\n')
        if flag==0:
            if value>0:
                rk.write(feat+'='+str(value)+'=4=1=0\n')
            else:
                rk.write(feat+'='+str(value)+'=4=0=1\n')
    implicit=str(file(imp,"r").read()).split('\n')
    for i in range(len(implicit)-1):
        flag=0
        temp=str(implicit[i]).split('[')
        feat=str(str(temp[1]).split(']')[0])
        temp=(str(temp[2]).split(':'))[1]
        value=int(temp)
        data=file('ranked.txt','r').read().split('\n')
        rk=file('ranked.txt','w')
        for j in range(len(data)-1):
            temp=str(data[j]).split('=')
            if feat==str(temp[0]) or feat in str(temp[0]) or str(temp[0]) in feat:
                flag=1
                temp[1]=value+int(temp[1])
                temp[2]=int(temp[2])+4
                if value>0:
                    temp[3]=int(temp[3])+1
                else:
                    temp[4]=int(temp[4])+1
            rk.write(str(temp[0])+'='+str(temp[1])+'='+str(temp[2])+'='+str(temp[3])+'='+str(temp[4])+'\n')
        if flag==0:
            if value>0:
                rk.write(feat+'='+str(value)+'=4=1=0\n')
            else:
                rk.write(feat+'='+str(value)+'=4=0=1\n')
    return

def check():
    try:
        file('ranked.txt','r')
    except:
        file('ranked.txt','w')
    return


if __name__=="__main__":
    rank("explicit.txt","implicit.txt")
