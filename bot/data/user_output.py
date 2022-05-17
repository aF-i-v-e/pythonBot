from bot.api import user_input
from bot.data import contribution


class UserOutput:
    __user_input = user_input.UserInput
    __final_amount_contribution = 0
    __contribution = contribution.Contribution

    def __init__(self, user_input, total_money_amount, best_contribution):
        self.__user_input = user_input
        self.__final_amount_contribution = total_money_amount
        self.__contribution = best_contribution

    def get_user_input(self):
        return self.__user_input

    def set_user_input(self, user_input):
        self.__user_input = user_input

    def get_final_amount_contribution(self):
        return self.__final_amount_contribution

    def set_final_amount_contribution(self, final_amount_contribution):
        self.__final_amount_contribution = final_amount_contribution

    def get_contribution(self):
        return self.__contribution

    def set_contribution(self, bank_contribution):
        self.__contribution = bank_contribution

    def get_string_representation(self):
        return self.__user_input.get_string_representation()\
               + self.__contribution.get_string_representation\
               + f"Итоговая сумма по данному вкладу будет составлять {self.__final_amount_contribution} рублей.\n"
