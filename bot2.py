

# Work with Python 3.6
import requests
from bs4 import BeautifulSoup
import random
import re
import discord
import random

TOKEN = 'NTc5NDAzNTgxOTEyOTA3Nzc3.XOBp0g.F4RgOcPCQ6cC4m3SqcZA8JcZhKg'

client = discord.Client()
start = 0
messagelist = {}
s = 0
x = 0



def synonym(word):
    if word.lower() == "i":
        return word
    url = "https://www.synonyms.com/synonym/" + word
    synonymlist = []

    r = requests.get(url)
    r_html = r.text
    page = BeautifulSoup(r_html, "html.parser")
    synonyms = page.select("p.syns a")

    for i in synonyms:
        word1 = ''
        for x in i:
            word1 += x
        synonymlist.append(word1)

    if len(synonymlist) > 0:
        return random.choice(synonymlist)
    else:
        return word


def synonymsentence(sentence):
    sentence = re.sub(r'[^\w\s]', '', sentence)
    sentence = sentence.split()
    newsentence = []
    for x in sentence:
        newsentence.append(synonym(x) + ' ')

    return ''.join(newsentence)



def rhyme(word):
    if word == 'bot':
        return random.choice(['hot', 'got', 'lot', 'apricot'])
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
    if len(rhymelist) > 0:
        return random.choice(rhymelist)
    else:
        return word

def rhymesentence(sentence):
    sentence = re.sub(r'[^\w\s]', '', sentence)
    sentence = sentence.split()
    newsentence = []
    for x in sentence:
        newsentence.append(rhyme(x) + ' ')

    return ''.join(newsentence)





@client.event
async def on_message(message):
    print(message.author)

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!@#$'):
        print(synonymsentence(message.content))
        await message.channel.send(synonymsentence(message.content))
    if message.content.startswith('$#@!'):
        print(rhymesentence(message.content))
        await message.channel.send(rhymesentence(message.content))





@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')





client.run(TOKEN)


