"""Класс, хранящий данные вклада"""


class Contribution:

    def __init__(self):
        self._percent = 0
        self._start_sum = 0
        self._months_number = 0
        self._bank_name = ""
        self._contribution_name = ""
        self._package_services_price = 0

    def __init__(self, percent, start_sum, months_number, bank_name, contribution_name, package_services_price):
        self._percent = percent
        self._start_sum = start_sum
        self._months_number = months_number
        self._bank_name = bank_name
        self._contribution_name = contribution_name
        self._package_services_price = package_services_price

    def get_percent(self):
        return self._percent

    def set_percent(self, contribution_percentage):
        self._percent = contribution_percentage

    def get_start_sum(self):
        return self._start_sum

    def set_start_sum(self, contribution_minimum_amount):
        self._start_sum = contribution_minimum_amount

    def get_months_number(self):
        return self._months_number

    def set_months_number(self, contribution_term):
        self._months_number = contribution_term

    def get_bank_name(self):
        return self._bank_name

    def set_bank_name(self, bank_name):
        self._bank_name = bank_name

    def get_contribution_name(self):
        return self._contribution_name

    def set_contribution_name(self, contribution_name):
        self._contribution_name = contribution_name

    def get_package_services_price(self):
        return self._package_services_price

    def set_package_services_price(self, service_price):
        self._package_services_price = service_price

    def equals(self, other_contribution):
        return (
                self._percent == other_contribution.get_percent()
                and self._start_sum == other_contribution.get_start_sum()
                and self._months_number == other_contribution.get_months_number()
                and self._bank_name == other_contribution.get_bank_name()
                and self._contribution_name == other_contribution.get_contribution_name()
                and self._package_services_price == other_contribution.get_package_services_price())

    def get_string_representation(self):
        return f"Банк: {self._bank_name}, " \
               f"Вклад: {self._contribution_name}, " \
               f"Процент: {self._percent}%, " \
               f"Срок вклада: {self._months_number}, " \
               f"Минимальная начальная сумма вклада: {self._start_sum} рублей, " \
               f"Стоимость пакета услуг: {self._package_services_price} рублей."
