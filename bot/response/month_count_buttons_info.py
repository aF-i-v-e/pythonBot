from bot.business_logic.logic_utils.divide_contributions import identify_suitable_contributions
from bot.data.contributions_manager import Parsing


def get_month_count_from_contributions(user_input):
    """ Получение отсортированного списка месяцев, в котором все элементы уникальны из вкладов,
    полученных при помощи парсинга

      Аргументы:

      user_input: Входные данные пользователя.

      """
    parsing = Parsing()
    contributions = parsing.get_list_contributions()
    suitable_contributions = identify_suitable_contributions(contributions, user_input)
    return get_month_count_list(suitable_contributions)


def get_month_count_list(suitable_contributions):
    """ Получение списка месяцев, в котором нет повторяющихся и элементы отсортированы в порядке возрастания

      Аргументы:

      suitable_contributions: подходящие для пользователя вклады

      """
    month_list = list(set(map(lambda contribution: contribution.get_months_number(), suitable_contributions)))
    month_list.sort()
    return month_list
