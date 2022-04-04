from banks_parsing import *


class Parsing:
    __list = []

    def get_list_contributions(self):
        alfa1 = Alfa1()
        self.__list.append(alfa1.get_contribution())
        self.__list.append(alfa1.get_contribution())
        # self.__list.append(VuzBank1.get_contribution())
        # print(self.__list)
        return self.__list
