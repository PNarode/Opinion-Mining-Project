import urllib
import sys
import re
 
def get(feature):
    synonym=[]
    antonym=[]
    url = 'http://sentistrength.wlv.ac.uk/results.php?text=' + feature 
    temp=urllib.urlopen(url).readlines()
    temp=str(temp[110]).split('<b>')
    pos=str(temp[1]).split('</b>')
    neg=str(temp[2]).split('</b>')
    pos=int(pos[0])
    neg=int(neg[0])
    return pos-1,neg+1


if __name__=='__main__':
    feat=raw_input("Enter the Adjective to get Strength:")
    pos,neg=get(feat)
    if pos>(0-neg):
        print feat," is positive adjective wit strength ",pos
    else:
        print feat," is negative adjective wit strength ",neg


