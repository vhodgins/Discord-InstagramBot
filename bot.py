

# Work with Python 3.6
import discord
import requests
import re
from bs4 import BeautifulSoup
import random

TOKEN = 'NTc5NDAzNTgxOTEyOTA3Nzc3.XOBp0g.F4RgOcPCQ6cC4m3SqcZA8JcZhKg'

client = discord.Client()
start = 0
messagelist = {}
s = 0
x = 0
@client.event
async def on_message(message):
    global s, x
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    print(message.author)

    if str(message.author) == "QuoteMan#8109":
        await message.channel.send('please stop talking Quote')

    if str(message.author) == "Wacky Schemes#1189":
        await message.channel.send('please talk more i love it')


    if message.content.startswith('!@#$'):


        def synonym(word):
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

            return random.choice(synonymlist)

        def synonymsentence(sentence):
            sentence = re.sub(r'[^\w\s]', '', sentence)
            sentence = sentence.split()
            newsentence = []
            for x in sentence:
                newsentence.append(synonym(x) + ' ')

            return ''.join(newsentence)

        print(synonymsentence(message.content))
        await message.channel.send(synonymsentence(message.content))


    global messagelist
    messagelist[message.id] = message.author.name

    if 'random message' in message.content.lower():
        user1 = ''
        usermessages = []
        user = str(message.content).split()
        for x in range(2, len(user)):
            user1 = user1 + ' ' + user[x]
        for c in messagelist:
            if user1.lower().strip() in messagelist[c].lower().strip():
                usermessages.append(c)
        mess = (await message.channel.fetch_message(usermessages[random.randrange(0, len(usermessages))]))
        await message.channel.send('One time' + str(user1) + ' said: ' + str(mess.content))

    if 'please count for me robertbot' in message.content:
        if x != 0:
            x = 0
        s = 1

    if message.content.startswith('please, oh please robertbot, stop counting, its awful and terrible.'):
        s = 0
        print(s)

    #await message.channel.send('please stop talking to me')

    while s == 1:
        await message.channel.send(x)
        x += 1




@client.event
async def on_message_delete(message):

    await message.channel.send("why did you delete that i was reading it")





@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_typing(channel,user,when):
    '''
    if str(user) == "QuoteMan#8109":
        await channel.send('please stop typing Quote')
    '''


    await channel.send(input())



client.run(TOKEN)
