# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 12:03:49 2018
@author: Sidhanta
"""
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os
from gtts import gTTS
import speech_recognition as sr
from pygame import mixer

r = sr.Recognizer()
bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('F:\chatbot\Chatterbot_corpus\chatterbot-corpus-master\chatterbot_corpus\data\english/'):
    data = open('F:\chatbot\Chatterbot_corpus\chatterbot-corpus-master\chatterbot_corpus\data\english/' + files,
                'r').readlines()
    bot.train(data)

while True:
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    message = str(r.recognize_google(audio))

    if message.strip() != 'Bye':
        reply = bot.get_response(message)
        mytext = str(reply)
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("welcome.mp3", 'wb')
        #        os.system("mpg321 welcome.mp3")
        mixer.init()
        mixer.music.load('welcome.mp3')
        mixer.music.play()
        print('Desi_Thanos:', reply)

    if message.strip() == 'Bye' or message.strip() == 'bye':
        print('Desi_Thanos:Bye')
        break