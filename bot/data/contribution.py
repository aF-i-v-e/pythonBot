class Contribution:
    __percent = 0
    __start_sum = 0
    __months_number = 0
    __bank_name = ""
    __contribution_name = ""
    __package_services_price = 0

    def __init__(self, percent, start_sum, month_number, bank_name, contribution_name, package_services_price):
        self.__percent = percent
        self.__start_sum = start_sum
        self.__months_number = month_number
        self.__bank_name = bank_name
        self.__contribution_name = contribution_name
        self.__package_services_price = package_services_price

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

    def equals(self, other_contribution):
        return (
                self.__percent == other_contribution.get_percent()
                and self.__start_sum == other_contribution.get_start_sum()
                and self.__months_number == other_contribution.get_months_number()
                and self.__bank_name == other_contribution.get_bank_name()
                and self.__contribution_name == other_contribution.get_contribution_name()
                and self.__package_services_price == other_contribution.get_package_services_price())

    def get_string_representation(self):
        return f"Банк: {self.__bank_name}, " \
               f"Вклад: {self.__contribution_name}, " \
               f"Процент: {self.__percent}%, " \
               f"Срок вклада: {self.__months_number}, " \
               f"Минимальная начальная сумма вклада: {self.__start_sum} рублей, " \
               f"Стоимость пакета услуг: {self.__package_services_price} рублей."
