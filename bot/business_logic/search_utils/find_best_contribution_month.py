from bot.business_logic.logic_utils.count_total_money_amount import count_contribution_total_money_amount
from bot.data.user_output import UserOutput


def find_best_contribution_month(contribution_dict, user_input):
    """Нахождение лучшего вклада с учетом заданного пользователем количества месяцев

        Аргументы:

        contribution_dict: Словарь, в котором
        ключ - количество месяцев, значение - список вкладов, у которых срок равен ключу

        user_input: user_input: Входные данные пользователя.
    """
    month_count = user_input.get_month_count()
    if not (month_count in contribution_dict):
        print(f"The specified number of months: {month_count} is not in the dictionary of deposits!")
        return None
    contributions = contribution_dict[month_count]
    if len(contributions) == 0:
        print("There are no suitable contributions for the user")
        return None
    return get_best_contribution_from_list(contributions, user_input)


def get_best_contribution_from_list(contributions, user_input):
    """Нахождение вклада с самой большой процентной ставкой

        Аргументы:

        contributions: Список вкладов
    """
    best_contribution = None
    best_result_amount = None
    for contribution in contributions:
        if best_contribution is None or contribution.get_percent() >= best_contribution.get_percent():
            result_contribution_amount = count_contribution_total_money_amount(user_input, contribution)
            if best_contribution is None or result_contribution_amount > best_result_amount:
                best_contribution = contribution
                best_result_amount = result_contribution_amount
    return UserOutput(user_input, best_result_amount, best_contribution)
