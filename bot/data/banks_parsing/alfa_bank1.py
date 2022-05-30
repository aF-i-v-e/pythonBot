from lxml import html
from bot.data import contribution
from bot.data.banks_parsing import connect

user_agent = {'User-agent': 'Mozilla/5.0'}

"""Парсинг Альфа Альфа-Вклад"""


class AlfaBank1:

    def __init__(self):
        self._bank_name = "Альфа Банк"
        self._bank_contribution = None
        self._url = "https://alfabank.ru/make-money/deposits/alfa/"
        self.contribution = contribution.Contribution()
        self._response = None

    def get_contribution(self):
        try:
            bank_info = connect.Connect(self._url, user_agent)
        except Exception:
            print(self.__class__.__name__, ": Ошибка подключения" + self._url)
            return None
        if bank_info.status_code == 200:
            self._response = html.fromstring(bank_info.response.text)
            self._bank_contribution = self._response.xpath(
                '//*[@id="main-banner"]/div/div/div/div/div[1]/div/div[1]/h1')[0].text
            self.contribution.set_percent(self.get_percent())
            self.contribution.set_start_sum(self.get_start_sum())
            self.contribution.set_months_number(self.get_months_number())
            self.contribution.set_bank_name(self.get_bank_name())
            self.contribution.set_contribution_name(self.get_contribution_name())
            self.contribution.set_package_services_price(self.get_package_services_price())
            return self.contribution
        else:
            print(self.__class__.__name__, ": status_code=" + str(bank_info.status_code) + " " + self._url)

    def get_percent(self):
        percent_text = self._response.xpath(
            '//*[@id="benefit-cards"]/div/div[1]/p[2]')[0].text_content()
        percent = percent_text.split(' ')[0].split('\xa0')[1]
        return float(percent.replace(',', '.')[:-1])

    def get_start_sum(self):
        start_sum_text = self._response.xpath(
            '//*[@id="calculator"]/div[2]/div/div[2]/div/div/div[1]/div[1]/div[2]/span[1]')[0].text_content()
        start_sum = start_sum_text.split(' ')
        return int(start_sum[0]) * 1000

    def get_months_number(self):
        months_number_text = self._response.xpath(
            '//*[@id="calculator"]/div[2]/div/div[2]/div/div/div[1]/div[2]/button[7]/p')[0].text_content()
        months_number = months_number_text.split(' ')[0]
        return int(months_number) * 12

    def get_bank_name(self):
        return self._bank_name

    def get_contribution_name(self):
        return self._bank_contribution

    def get_package_services_price(self):
        return 0
