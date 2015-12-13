#coding: utf-8

from telegram import Updater

updater = Updater(token='162792644:AAFees4-i0i0svFyEv3lU5tOmQM-UrPo2zE')
dispatcher = updater.dispatcher

def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Je suis un bot qui peut parler")

def affiche(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="bientot je pourrai vous afficher les jobs")

def trieremplois(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="bientot je pourrai meme vous envoyer toute une liste de jobs trier ^^ ")	

def echo(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

def unknown(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text= u"OUPS!!! Désolé je ne comprend pas cette commande.")


dispatcher.addTelegramCommandHandler('start', start)
dispatcher.addTelegramCommandHandler('affiche', affiche)
dispatcher.addTelegramCommandHandler('trieremplois', trieremplois)
dispatcher.addUnknownTelegramCommandHandler(unknown)
dispatcher.addTelegramMessageHandler(echo)

updater.start_polling()