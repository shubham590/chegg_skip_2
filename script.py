from email import header
import traceback

from requests import head

from analyze import Analyze
from chegg import Chegg
from utils import clear_screen, random_long_wait, random_wait, welcome_banner,log
import yaml

clear_screen()
welcome_banner()
config = ''
try:
    with open("config.yaml", "r") as yamlfile:
        config = yaml.load(yamlfile, Loader=yaml.FullLoader)
        log("Reading config.yaml file successfully")
except FileNotFoundError:
    log("config.yaml file not found.Contact the developer or re-install!!")
    exit()

if not config.get('cookie'):
    log('Set the cookie in config.yaml file')
headers = {'cookie': config.get('cookie')}
keywords = config.get('keywords',[])
count = 0
try:
    while True:
        bot = Chegg(headers=headers, keywords=keywords)
        bot.fetch_question()
        random_wait()
        if not bot.question:
            log("No questions left.")
            count = 0
            random_long_wait()
            continue
        else:
            if(count == 0):
                bot.answer_question()
                count = 1
            
except Exception as e:
    traceback.print_exc()
