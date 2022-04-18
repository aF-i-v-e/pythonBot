from lxml import html
from bot.data import contribution
from bot.data.banks_parsing import connect
from bot.data.banks_parsing import fill_fields_contributions
import copy

user_agent = {'User-agent': 'Mozilla/5.0'}


class VuzBank2:
    __bank_name = ""
    __bank_contribution = ""
    __url = ""
    contribution = None
    __response = ""
    contributions = []

    def __init__(self):
        self.__bank_name = "Вуз Банк"
        self.__url = "https://www.vuzbank.ru/chastnym-klientam/vklady/udobnyy"
        self.contribution = contribution.Contribution()

    def get_contributions(self):
        bank_info = connect.Connect(self.__url, user_agent)
        if bank_info.status_code == 200:
            self.__response = html.fromstring(bank_info.response.text)
            self.__bank_contribution = self.__response.xpath('//*[@id="workarea"]/div[1]/div[2]/div/h1')[0].text
            fill_fields_contributions.FillFiledContributions(self)
            self.fill_percent()
            self.fill_months_numbers()
            return self.contributions
        else:
            print(self.__class__.__name__, ": status_code=" + str(bank_info.status_code))

    def get_percent(self):
        percents_text = self.__response.xpath(
            '//*[@id="workarea"]/div[6]/div/div/div/div/div[1]/div[3]/div/table/tbody/tr[1]/td[2]/p')[
            0].text_content()
        percents = percents_text.split(' ')
        return float(percents[1].replace(',', '.')[:len(percents)])

    def get_start_sum(self):
        start_sum_text = self.__response.xpath(
            '//*[@id="workarea"]/div[6]/div/div/div/div/div[1]/div[3]/div/table/tbody/tr[7]/td[2]/p')[
            0].text_content()
        start_sum = start_sum_text.split(' ')
        return int(start_sum[0] + start_sum[1])

    def get_months_number(self):
        months_number_text = self.__response.xpath(
            '//*[@id="workarea"]/div[6]/div/div/div/div/div[1]/div[3]/div/table/tbody/tr[6]/td[2]/p')[0]
        months_number_list = []
        months_number_int = int(months_number_text.text_content().split(' ')[0])
        months_number_list.append(months_number_int)
        return months_number_list

    def get_bank_name(self):
        return self.__bank_name

    def get_contribution_name(self):
        return self.__bank_contribution

    def get_package_services_price(self):
        package_services_price_text = self.__response.xpath(
            '//*[@id="accordion-1"]/div/div/div[1]/div/table/tbody/tr[9]/td[2]/p')
        package_services_price = ''.join(package_services_price_text[0].text_content().split(' ')[0].split('\xa0'))
        return int(package_services_price)

    def fill_months_numbers(self):
        months_number_list = self.get_months_number()
        for months_number in months_number_list:
            contribution = copy.deepcopy(self.contribution)
            contribution.set_months_number(months_number)
            self.contributions.append(contribution)

    def fill_percent(self):
        self.contribution.set_percent(self.get_percent())
