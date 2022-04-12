class Contribution:
    __percent = 0
    __start_sum = 0
    __months_number = 0
    __replenishment_in_process = False
    __bank_name = ""
    __contribution_name = ""
    __package_services_price = 0

    def get_percent(self):
        return self.__percent

    def set_percent(self, contribution_percentage):
        self.__percent = contribution_percentage

    def get_start_sum(self):
        return self.__start_sum

    def set_start_sum(self, contribution_minimum_amount):
        self.__start_sum = contribution_minimum_amount

    def get_months_number(self):
        return self.__months_number

    def set_months_number(self, contribution_term):
        self.__months_number = contribution_term

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

    def get_package_services_price(self):
        return self.__package_services_price

    def set_package_services_price(self, service_price):
        self.__package_services_price = service_price
