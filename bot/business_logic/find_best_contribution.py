from bot.business_logic.logic_utils.divide_contributions import identify_suitable_contributions, divide_contributions
from bot.business_logic.search_utils.find_best_contribution_from_all import find_best_contribution_from_all
from bot.business_logic.search_utils.find_best_contribution_month import find_best_contribution_month


def find_best_contribution(all_deposits, user_input):
    """Нахождение лучшего вклада.

    Аргументы:

    all_deposits: Список всех вкладов.

    user_input: Входные данные пользователя.

    Возвращает:

    Лучший вклад по количеству денег, которые можно получить в конце срока вклада с
    учётом стоимости пакета услуг
    """
    user_amount = user_input.get_amount()
    suitable_contributions = identify_suitable_contributions(all_deposits, user_amount)
    if len(suitable_contributions) == 0:
        print("There are no suitable contributions for the user")
        return None
    contributions_dict = divide_contributions(suitable_contributions)
    if user_input.get_month_count() == 0:
        return find_best_contribution_from_all(contributions_dict, user_input)
    return find_best_contribution_month(contributions_dict, user_input)
