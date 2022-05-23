from bot.data.banks_parsing import *

"""Класс, который отвечает за получение информации о вкладах бакнов"""


class ContributionManager:

    def __init__(self):
        self._list = []

    """Возвращает массив вкладов бакнов"""

    def get_list_contributions(self):
        # alfa1 = Alfa1()
        # self._list.extend(alfa1.get_contributions())
        vuz_bank1 = VuzBank1()
        v_z_1 = vuz_bank1.get_contributions()
        self.try_add_contributions(v_z_1)
        vuz_bank2 = VuzBank2()
        self.try_add_contributions(vuz_bank2.get_contributions())
        vuz_bank3 = VuzBank3()
        self.try_add_contributions(vuz_bank3.get_contributions())
        print(self._list)
        return self._list

    """Добавляет вклад в список, если он корректен"""

    def try_add_contributions(self, contributions):
        if contributions is not None:
            self._list.append(contributions)


cm = ContributionManager()
cm.get_list_contributions()
print()
