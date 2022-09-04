import requests, json, telebot


url = "https://rewriter-paraphraser-text-changer-multi-language.p.rapidapi.com/rewrite"
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "916276f6d0mshf754451bf6d248dp13dc4ajsnb3cf7cb20768",
	"X-RapidAPI-Host": "rewriter-paraphraser-text-changer-multi-language.p.rapidapi.com"
}


apit = "5659874037:AAHJOJd0GdGwLBBOwJBzj_NQwGnIrdSAMiM"

bot = telebot.TeleBot(apit)

def gen(text):
   ftext = f"""{text}"""
   payload = {
	"language": "id",
	"strength": 3,
	"text": text
   }
   js = requests.post(url, json=payload, header=header).text
   f = json.loads(js)
   return f["rewrite]



@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
   bot.reply_to(message, """\
Hi zaa""")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
   rw = gen(message.text)
   bot.reply_to(message, gen)


bot.infinity_polling()
