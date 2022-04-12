from lxml import html
from bot.data import contribution
from bot.data.banks_parsing import connect
from bot.data.banks_parsing import fill_fields_contributions

user_agent = {'User-agent': 'Mozilla/5.0'}


class VuzBank1:
    __bank_name = "Вуз Банк"
    __bank_contribution = "Надёжный"
    __url = 'https://www.vuzbank.ru/chastnym-klientam/vklady/nakopitelnyy'
    contribution = contribution.Contribution()
    __response = ""
    contributions = []

    def get_contributions(self):
        bank_info = connect.Connect(self.__url, user_agent)
        if bank_info.status_code == 200:
            self.__response = html.fromstring(bank_info.response.text)
            fill_fields_contributions.FillFiledContributions(self)
            return self.contributions
        else:
            print(self.__class__.__name__, ": status_code=" + str(bank_info.status_code))

    def get_percent(self):
        percents_text = self.__response.xpath(
            '//*[@id="workarea"]/div[6]/div/div/div/div/div[1]/div[3]/div/table/tbody/tr[1]/td[2]/div/ul/li[1]')[
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
            '//*[@id="workarea"]/div[6]/div/div/div/div/div[1]/div[3]/div/table/tbody/tr[6]/td[2]/div/ul')[0]
        months_number_list = []
        for months_number in months_number_text:
            months_number_list.append(int(months_number.text_content().split(' ')[0]))
        return months_number_list

    def get_replenishment_in_process(self):
        return True

    def get_bank_name(self):
        return self.__bank_name

    def get_contribution_name(self):
        return self.__bank_contribution

    def get_package_services_price(self):
        package_services_price_text = self.__response.xpath(
            '//*[@id="accordion-1"]/div/div/div[1]/div/table/tbody/tr[9]/td[2]/p')
        package_services_price = ''.join(package_services_price_text[0].text_content().split(' ')[0].split('\xa0'))
        return int(package_services_price)
