#main applikation
#Funktions
#Grap an Image from the gopro
#Post by telegrom

import telegramBot

print "Welcome to the fotobox app"

print "send status message"
telegramBot.get_client_ids()
telegramBot.send_message('hello from bot')
telegramBot.send_image('/home/pascal/Pictures/mila.jpg')


