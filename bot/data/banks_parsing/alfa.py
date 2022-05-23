from lxml import html
from bot.data import contribution
from bot.data.banks_parsing import connect

user_agent = {'User-agent': 'Mozilla/5.0'}


class Alfa1:
    _url = "https://alfabank.ru/make-money/savings-account/alfa/"
