#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple grammar checker

This grammar checker will fix grammar mistakes using Ginger.
"""

import sys
import urllib
import urlparse
from urllib2 import HTTPError
from urllib2 import URLError
import json
from nltk.tokenize import sent_tokenize

out=""

def get_ginger_url(text):
    """Get URL for checking grammar using Ginger.
    @param text English text
    @return URL
    """
    API_KEY = "6ae0c3a0-afdc-4532-a810-82ded0054236"

    scheme = "http"
    netloc = "services.gingersoftware.com"
    path = "/Ginger/correct/json/GingerTheText"
    params = ""
    query = urllib.urlencode([
        ("lang", "US"),
        ("clientVersion", "2.0"),
        ("apiKey", API_KEY),
        ("text", text)])
    fragment = ""

    return(urlparse.urlunparse((scheme, netloc, path, params, query, fragment)))


def get_ginger_result(text):
    """Get a result of checking grammar.
    @param text English text
    @return result of grammar check by Ginger
    """
    url = get_ginger_url(text)

    try:
        response = urllib.urlopen(url)
    except HTTPError as e:
            print("HTTP Error:", e.code)
            quit()
    except URLError as e:
            print("URL Error:", e.reason)
            quit()

    try:
        result = json.loads(response.read().decode('utf-8'))
    except ValueError:
        print("Value Error: Invalid server response.")
        quit()
    return(result)


def ginger(text):
    results = get_ginger_result(text)
    if(not results["LightGingerTheTextResult"]):
        if len(text)!=0:
            data=str(file("corrected.txt","r").read())
            data+=text+"\n"
            file("corrected.txt","w").write(data)
            return
    else:
        for result in results["LightGingerTheTextResult"]:
            if(result["Suggestions"]):
                from_index = result["From"]
                to_index = result["To"] + 1
                suggest = result["Suggestions"][0]["Text"]
                if text[:from_index]==" ":
                    fixed_text=suggest+text[to_index:]
                elif text[to_index:]==" ":
                    fixed_text=text[:from_index]+suggest
                else:
                    fixed_text=text[:from_index]+suggest+text[to_index:]
        ginger(fixed_text)
            
def main(filename):
    file("corrected.txt","w")
    sent=sent_tokenize(file(filename,"r").read())
    for i in range(len(sent)):
        ginger(sent[i])
