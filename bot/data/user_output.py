import user_input
import contribution


class UserOutput:
    __user_input = user_input.UserInput
    __final_amount_contribution = 0
    __contribution = contribution.Contribution

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
