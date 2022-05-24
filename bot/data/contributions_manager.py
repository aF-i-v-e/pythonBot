from bot.data.banks_parsing import *

"""Класс, который отвечает за получение информации о вкладах бакнов"""


class ContributionManager:

    def __init__(self):
        self._list = []

    """Возвращает массив вкладов банков"""

    def get_list_contributions(self):
        # alfa1 = Alfa1()
        # self._list.extend(alfa1.get_contributions())
        vuz_bank1 = VuzBank1()
        v_z_1 = vuz_bank1.get_contribution()
        self.try_add_contributions(v_z_1)
        vuz_bank2 = VuzBank2()
        self.try_add_contributions(vuz_bank2.get_contribution())
        vuz_bank3 = VuzBank3()
        self.try_add_contributions(vuz_bank3.get_contribution())
        print(self._list)
        return self._list

    """Добавляет вклад в список, если он корректен"""

    def try_add_contributions(self, contribution):
        if contribution is not None:
            if not contribution.get_percent() or not isinstance(contribution.get_percent(), (float, int)):
                self.error_message(contribution)
                return
            if not contribution.get_start_sum() or not isinstance(contribution.get_start_sum(), int):
                self.error_message(contribution)
                return
            if not contribution.get_months_number() or not isinstance(contribution.get_months_number(), int):
                self.error_message(contribution)
                return
            if not contribution.get_months_number() or not isinstance(contribution.get_months_number(), int):
                self.error_message(contribution)
                return
            if not contribution.get_contribution_name() or not isinstance(contribution.get_contribution_name(), str):
                self.error_message(contribution)
                return
            if not isinstance(contribution.get_package_services_price(), int):
                self.error_message(contribution)
                return
            self._list.append(contribution)

    """Вывод сообщения о некорректности вклада"""

    def error_message(self, contribution):
        print("Вклад некорректен " + contribution.get_bank_name() + " " + contribution.get_contribution_name())


# cm = ContributionManager()
# cm_list = cm.get_list_contributions()
# print()
