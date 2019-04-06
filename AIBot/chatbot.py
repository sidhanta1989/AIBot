# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 12:03:49 2018

@author: Home
"""
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os


bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)


for files in os.listdir('F:\chatbot\Chatterbot_corpus\chatterbot-corpus-master\chatterbot_corpus\data\english/'):
	data = open('F:\chatbot\Chatterbot_corpus\chatterbot-corpus-master\chatterbot_corpus\data\english/'+files,'r').readlines()
	bot.train(data)



while True:
    message = input("Please Ask Something:")
    if message.strip() != 'Bye':
    	reply = bot.get_response(message)
    	print('Desi_Thanos:', reply)


    if message.strip() == 'Bye':
    	print('Desi_Thanos:Bye')
    	break