class Contribution:
    __contribution_percentage = 0
    __contribution_minimum_amount = 0
    __contribution_term = 0
    __replenishment_in_process = False
    __bank_name = ""
    __contribution_name = ""
    __service_price = 0

    def get_contribution_percentage(self):
        return self.__contribution_percentage

    def set_contribution_percentage(self, contribution_percentage):
        self.__contribution_percentage = contribution_percentage

    def get_contribution_minimum_amount(self):
        return self.__contribution_minimum_amount

    def set_contribution_minimum_amount(self, contribution_minimum_amount):
        self.__contribution_minimum_amount = contribution_minimum_amount

    def get_contribution_term(self):
        return self.__contribution_term

    def set_contribution_term(self, contribution_term):
        self.__contribution_term = contribution_term

    def get_replenishment_in_process(self):
        return self.__replenishment_in_process

    def set_replenishment_in_process(self, replenishment_in_process):
        self.__replenishment_in_process = replenishment_in_process

    def get_bank_name(self):
        return self.__bank_name

    def set_bank_name(self, bank_name):
        self.__bank_name = bank_name

    def get_contribution_name(self):
        return self.__contribution_name

    def set_contribution_name(self, contribution_name):
        self.__contribution_name = contribution_name

    def get_service_price(self):
        return self.__service_price

    def set_service_price(self, service_price):
        self.__service_price = service_price
