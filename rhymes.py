import requests
import re
from bs4 import BeautifulSoup
import random


def rhyme(word):
    url = "https://www.rhymezone.com/r/rhyme.cgi?Word="+word+"&typeofrhyme=perfect&org1=syl&org2=l&org3=y"
    r = requests.get(url)
    r_html = r.text
    page = BeautifulSoup(r_html, "html.parser")
    rhymes = page.select("a.d")
    rhymelist = []
    for i in rhymes:
        word1 = ''
        for x in i:
            word1 += x
        rhymelist.append(word1)
    return random.choice(rhymelist)

def rhymesentence(sentence):
    sentence = re.sub(r'[^\w\s]', '', sentence)
    sentence = sentence.split()
    newsentence = []
    for x in sentence:
        newsentence.append(rhyme(x) + ' ')

    return ''.join(newsentence)




