# здесь нужен импорт модуля, содержащего в себе класс UserOutput

def find_profitable_deposit(all_deposits, user_input):
    """Нахождение лучшего вклада.

    Аргументы:

    all_deposits: Список всех вкладов.

    user_input: Начальная сумма вклада пользователя.

    Возвращает:

    Лучший вклад по количеству денег, которые можно получить в конце срока вклада.
    """
    user_amount = user_input.amount
    suitable_contributions = identify_suitable_contributions(all_deposits, user_amount)
    best_deposit_info = find_profitable_deposit_info(suitable_contributions)
    return UserOutput(user_input, best_deposit_info[0], best_deposit_info[1])

def find_profitable_deposits(all_deposits, user_input):
    """Нахождение нескольких лучших вкладов.

    Аргументы:

    all_deposits: Список всех вкладов.

    user_input: Начальная сумма вклада пользователя.

    Возвращает:

    Список лучших вкладов по количеству денег, которые можно получить в конце срока вклада, с учетом выбора
    количества месяцев.
    """
    user_amount = user_input.amount
    suitable_contributions = identify_suitable_contributions(all_deposits, user_amount)
    contrib_dict = divide_contributions(suitable_contributions)
    best_contributions_info = get_best_contributions_info(contrib_dict)
    user_output = []
    for contribution_info in best_contributions_info:
        output = UserOutput(user_input, contribution_info[0], contribution_info[1])
        user_output.append(output)
    return user_output


def divide_contributions(suitable_contributions):
    """Разделение вкладов на группы по количеству месяцев.

    Аргументы:

    suitable_contributions: Список вкладов, подходящих пользователю.

    Возвращает:

    Словарь, в котором ключом является количество месяцев, а значением -
    список вкладов со сроком, равным этому количеству месяцев.
    """
    dictionary = dict()
    for contribution in suitable_contributions:
        month_number = contribution.months_number
        if month_number in dictionary:
            dictionary.get(month_number).append(contribution)
        else:
            dictionary[month_number] = [contribution]
    return dictionary


def get_best_contributions_info(dictionary):
    """Нахождение .

    Аргументы:

    suitable_contributions: Список вкладов, подходящих пользователю.

    Возвращает:

    Словарь, в котором ключом является количество месяцев, а значением -
    список вкладов со сроком, равным этому количеству месяцев.
    """
    best_contributions_info = []
    for month in dictionary:
        contributions = dictionary[month]
        best = find_profitable_deposit_info(contributions)
        best_contributions_info.append(best)
    return best_contributions_info


def get_total_money_amount(start_sum, percent, months_number):
    """Вычисление итоговой суммы денег, которую получит пользователь в конце срока вклада.

    Аргументы:

    start_sum: Начальная сумма клада.

    percent: Процент, который начисляется каждый месяц на сумму вклада.

    months_number: Срок действия вклада.

    Возвращает:

    Сумма денег, которую получит пользователь в конце срока действия вклада.
    """
    return ((1 + percent / 100) ** months_number) * start_sum


def identify_suitable_contributions(all_deposits, user_amount):
    """Нахождение подходящих вкладов для пользователя. Вклад считается подходящим, если сумма денег,
     которую пользователь хочет положить в банк, больше либо равна начальной сумме вклада.

     Аргументы:
     all_deposits: Список всех вкладов.

     user_amount: Начальная сумма вклада пользователя.
     Возвращает:

     Список вкладов, подходящих пользователю.
     """
    return list(filter(lambda deposit: user_amount >= deposit.minimum_amount, all_deposits))


def find_profitable_deposit_info(contributions):
    """Нахождение информации о лучшем вкладе из списка вкладов.

    Аргументы:

    contributions: Список вкладов.

    Возвращает:

    Максимальная сумма, которую можно получить в конце срока вклада, и  вклад,
    который даёт максимальную сумму вконце своего срока.
    """
    max_deposit_amount = 0
    best_deposit = contributions[0]
    for contribution in contributions:
        total_money_amount = get_total_money_amount(contribution.start_sum, contribution.percent,
                                                    contribution.months_number)
        resulting_sum = total_money_amount - contribution.package_services_price
        if resulting_sum > max_deposit_amount:
            max_deposit_amount = resulting_sum
            best_deposit = contribution
    return max_deposit_amount, best_deposit
