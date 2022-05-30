from lxml import html
from bot.data import contribution
from bot.data.banks_parsing import connect

user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 [ip:95.252.46.78]'}

"""Парсинг Синара Вклад Обыкновенное чудо!"""


class SinaraBank2:

    def __init__(self):
        self._bank_name = "Синара Банк"
        self._bank_contribution = None
        self._url = "https://skbbank.ru/chastnym-licam/vklady/obyknovennoe-chudo"
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
            self._bank_contribution = self._response.xpath('/html/body/div[3]/section/div[1]/div[3]/h1'
                                                           )[0].text_content()
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
        percents_text = self._response.xpath(
            '/html/body/div[3]/section/div[1]/div[3]/div[2]/div[1]/div[1]/span[2]'
        )[0].text_content()
        return float(percents_text.replace(',', '.')[:-1])

    def get_start_sum(self):
        start_sum_text = self._response.xpath(
            '/html/body/div[3]/section/div[1]/div[3]/div[2]/div[2]/div[1]/span[2]'
        )[0].text_content()
        start_sum = start_sum_text.split(' ')
        return int(start_sum[0] + start_sum[1])

    def get_months_number(self):
        months_number_text = self._response.xpath(
            '//*[@id="result"]/div[1]/div[3]/div[2]'
        )[0].text_content()
        months_number = months_number_text.replace(' ', '').replace('\n', '')[:3]
        return int(int(months_number) / 30)

    def get_bank_name(self):
        return self._bank_name

    def get_contribution_name(self):
        return self._bank_contribution

    def get_package_services_price(self):
        return 0
