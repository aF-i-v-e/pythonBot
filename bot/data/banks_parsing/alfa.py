from lxml import html
from bot.data import contribution
from bot.data.banks_parsing import connect
from bot.data.banks_parsing import fill_fields_contributions

user_agent = {'User-agent': 'Mozilla/5.0'}


class Alfa1:
    __url = "https://alfabank.ru/make-money/savings-account/alfa/"
