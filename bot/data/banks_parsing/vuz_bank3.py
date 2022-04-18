from lxml import html
from bot.data import contribution
from bot.data.banks_parsing import connect
from bot.data.banks_parsing import fill_fields_contributions
import copy

user_agent = {'User-agent': 'Mozilla/5.0'}


class VuzBank3:
    __bank_name = ""
    __bank_contribution = ""
    __url = ""
    contribution = None
    __response = ""
    contributions = []

    def __init__(self):
        self.__bank_name = "Вуз Банк"
        self.__url = "https://www.vuzbank.ru/chastnym-klientam/vklady/dohod-na-maksimum"
        self.contribution = contribution.Contribution()

    def get_contributions(self):
        bank_info = connect.Connect(self.__url, user_agent)
        if bank_info.status_code == 200:
            self.__response = html.fromstring(bank_info.response.text)
            self.__bank_contribution = self.__response.xpath('//*[@id="workarea"]/div[1]/div[2]/div/h1')[0].text
            fill_fields_contributions.FillFiledContributions(self)
            self.fill_percent_and_months_numbers()
            return self.contributions
        else:
            print(self.__class__.__name__, ": status_code=" + str(bank_info.status_code))

    def get_percents(self):
        percents_text = self.__response.xpath(
            '//*[@id="workarea"]/div[5]/div/div/div/div/div[3]/div/table/tbody/tr[1]')[0]
        percent_list = []
        for i in range(1,  3):
            percent = percents_text[i].text_content()
            percent_list.append(percent.replace(',', '.')[:len(percent) - 1])
        return percent_list

    def get_start_sum(self):
        start_sum_text = self.__response.xpath(
            '//*[@id="workarea"]/div[5]/div/div/div/div/div[2]/div/table/tbody/tr[4]/td[2]/p')[0].text_content()
        start_sum = start_sum_text.split(' ')
        return int(start_sum[0] + start_sum[1])

    def get_months_number(self):
        months_number_text = self.__response.xpath(
            '//*[@id="workarea"]/div[5]/div/div/div/div/div[3]/div/table/thead/tr[2]')[0]
        months_number_list = []
        for months_number in months_number_text:
            months_number_list.append(int(months_number.text_content()))
        return months_number_list

    def get_bank_name(self):
        return self.__bank_name

    def get_contribution_name(self):
        return self.__bank_contribution

    def get_package_services_price(self):
        # package_services_price_text = self.__response.xpath(
        #     '//*[@id="accordion-1"]/div/div/div[1]/div/table/tbody/tr[9]/td[2]/p')
        # package_services_price = ''.join(package_services_price_text[0].text_content().split(' ')[0].split('\xa0'))
        return 0 # int(package_services_price)

    def fill_percent_and_months_numbers(self):
        percent_list = self.get_percents()
        months_number_list = self.get_months_number()
        for i in range(0,  len(percent_list)):
            contribution = copy.deepcopy(self.contribution)
            contribution.set_percent(percent_list[i])
            contribution.set_months_number(months_number_list[i])
            self.contributions.append(contribution)
