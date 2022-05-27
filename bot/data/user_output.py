from bot.api import user_input
from bot.data import contribution

"""Класс, который хранит информацию о том, что выведем пользователю

    Аргументы:

    user_input: Информация о введенных пользователем данных
    total_money_amount: Конечная сумма вклада
    contribution: Информация о вкладе
"""


class UserOutput:

    def __init__(self, user_input=user_input.UserInput("", 0, 0), total_money_amount=0, contribution=contribution.Contribution()):
        self._user_input = user_input
        self._total_money_amount = total_money_amount
        self._contribution = contribution

    def get_user_input(self):
        return self._user_input

    def set_user_input(self, user_input):
        self._user_input = user_input

    def get_total_money_amount(self):
        return self._total_money_amount

    def set_total_money_amount(self, final_amount_contribution):
        self._total_money_amount = final_amount_contribution

    def get_contribution(self):
        return self._contribution

    def set_contribution(self, bank_contribution):
        self._contribution = bank_contribution

    def get_string_representation(self):
        return str(self._user_input.get_string_representation())\
               + str(self._contribution.get_string_representation())\
               + f"Итоговая сумма по данному вкладу будет составлять {self._total_money_amount} рублей.\n"
