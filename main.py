import time
import telepot
from telepot.loop import MessageLoop

from WebDriver import WebDriver


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage("-1001622522761", msg['text'])


TOKEN = "5373614449:AAG6TSr9TN3b2ZKHYTuse1Lf3Y25x_Rc4ZA"

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print('Listening ...')


# Keep the program running.
class DBChannel:
    def __init__(self):
        self.urls = []
        self.word = ""
        self.connection = None

    def setUrls(self, urls, word):
        self.urls = urls
        self.word = word

    def insert(self):
        print("")


def getUrls(words):
    driver = WebDriver()
    dbChannel = DBChannel()
    for word in words:
        driver.setWord(word)
        link = driver.getlinks()
        dbChannel.setUrls(link, word)
        dbChannel.insert()


def getWords():
    return ["isfahan", "tehran", "yazd"]


while 1:
    time.sleep(10)
    getUrls(getWords())
