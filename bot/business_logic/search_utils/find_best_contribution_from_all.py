from bot.business_logic.search_utils.find_best_contribution_month import get_best_contribution_from_list
from bot.data.user_output import UserOutput



def find_best_contribution_from_all(contribution_dict, user_input):
    """Нахождение лучшего вклада из всех доступных вкладов

       Аргументы:

       contribution_dict: Словарь, в котором
       ключ - количество месяцев, значение - список вкладов, у которых срок равен ключу

       user_input: user_input: Входные данные пользователя.
    """
    result_contribution = None
    result_money_amount = None
    result_profit_per_month = None
    for key, value in contribution_dict.items():
        if len(value) == 0:
            continue
        user_output = get_best_contribution_from_list(value, user_input)
        contribution_money_amount = user_output.get_final_amount_contribution()
        profit_per_month = contribution_money_amount / key

        if result_contribution is None or profit_per_month > result_profit_per_month:
            result_contribution = user_output.get_contribution()
            result_money_amount = contribution_money_amount
            result_profit_per_month = profit_per_month
    if result_contribution is None:
        print("There are no suitable contributions for the user")
        return None
    return UserOutput(user_input, result_money_amount, result_contribution)