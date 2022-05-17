def divide_contributions(suitable_contributions):
    """Разделение вкладов на группы по количеству месяцев, в течение которых начисляется процент

    Аргументы:

    suitable_contributions: Список вкладов, подходящих пользователю.

    Возвращает:

    Словарь, в котором ключом является количество месяцев, а значением -
    список вкладов со сроком, равным этому количеству месяцев.
    """
    dictionary = dict()
    for contribution in suitable_contributions:
        month_number = contribution.get_months_number()
        if month_number in dictionary:
            dictionary.get(month_number).append(contribution)
        else:
            dictionary[month_number] = [contribution]
    return dictionary


def identify_suitable_contributions(all_contributions, user_amount):
    """Нахождение подходящих вкладов для пользователя. Вклад считается подходящим, если сумма денег,
     которую пользователь хочет положить в банк, больше либо равна начальной сумме вклада.

     Аргументы:
     all_deposits: Список всех вкладов.

     user_amount: Начальная сумма вклада пользователя.
     Возвращает:

     Список вкладов, подходящих пользователю.
     """
    return list(filter(lambda contribution: user_amount >= contribution.get_start_sum(), all_contributions))
