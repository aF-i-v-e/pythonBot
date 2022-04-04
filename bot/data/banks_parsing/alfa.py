from lxml import html
from bot.data import contribution
from bot.data.banks_parsing import connect
from bot.data.banks_parsing import fill_fields_contributions

user_agent = {'User-agent': 'Mozilla/5.0'}


class Alfa1:
    url = "https://alfabank.ru/make-money/savings-account/alfa/"
    contribution = contribution.Contribution()
    response = ""

    def get_contribution(self):
        bank_connection = connect.Connect(self.url, user_agent)
        if bank_connection.status_code == 200:
            self.response = bank_connection.response.text
            fill_fields_contributions.FillFiledContributions(self)
            return self.contribution
        else:
            print(self.__class__.__name__, ": status_code=" + str(bank_connection.status_code))

    def get_contribution_percentage(self):
        return 1

    def get_contribution_minimum_amount(self):
        return 1

    def get_contribution_term(self):
        return 1

    def get_replenishment_in_process(self):
        return True

    def get_bank_name(self):
        return ""

    def get_contribution_name(self):
        return ""

    def get_service_price(self):
        return 1

        # print(response.text)
        # htmlContent = html.fromstring(response.text)
        # print(htmlContent.xpath('//img'))
