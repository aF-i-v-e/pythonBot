from bot.data.banks_parsing import *


class Parsing:
    __list = []

    def get_list_contributions(self):
        # alfa1 = Alfa1()
        # self.__list.extend(alfa1.get_contributions())
        vuz_bank1 = VuzBank1()
        self.__list.extend(vuz_bank1.get_contributions())
        vuz_bank2 = VuzBank2()
        self.__list.extend(vuz_bank2.get_contributions())
        vuz_bank3 = VuzBank3()
        self.__list.extend(vuz_bank3.get_contributions())
        # print(self.__list)
        return self.__list


# parsing = Parsing()
# parsing.get_list_contributions()
# print()
