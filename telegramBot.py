import telegram
bot = telegram.Bot(token='333340003:AAEN6_M8wS7GpeUACbuLqi-DSlQQjmo_LCo')
#telegramBot

ids = list()

def helloWorld():
	print("hello welt")

def get_client_ids():
	updates = bot.get_updates()
	for item in updates:
		id = item['message']['chat']['id']
		if id not in ids:
			ids.append(id)

def send_message(message):
	for id in ids:
		bot.send_message(id, message)

def send_image(path):
	for id in ids:
		bot.send_photo(id, photo=open(path, 'rb'))