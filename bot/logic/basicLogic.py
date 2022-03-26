# здесь нужен импорт модуля, содержащего в себе класс UserOutput

# первый режим работы: возвращаем лучший вклад по кол-ву полученных денег
def find_profitable_deposit(all_deposits, user_input):
    user_amount = user_input.amount
    suitable_contributions = identify_suitable_contributions(all_deposits, user_amount)
    best_deposit_info = find_profitable_deposit_info(suitable_contributions)
    return UserOutput(user_input, best_deposit_info[0], best_deposit_info[1])


# второй режим работы: возвращаем несколько лучших вкладов с учетом выбора кол-ва месяцев
def find_profitable_deposits(all_deposits, user_input):
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
    dictionary = dict()
    for contribution in suitable_contributions:
        month_number = contribution.months_number
        if month_number in dictionary:
            dictionary.get(month_number).append(contribution)
        else:
            dictionary[month_number] = [contribution]
    return dictionary


def get_best_contributions_info(dictionary):
    best_contributions_info = []
    for month in dictionary:
        contributions = dictionary[month]
        best = find_profitable_deposit_info(contributions)
        best_contributions_info.append(best)
    return best_contributions_info


def get_total_money_amount(start_sum, percent, months_number):
    return ((1 + percent / 100) ** months_number) * start_sum


def identify_suitable_contributions(all_deposits, user_amount):
    return list(filter(lambda deposit: user_amount >= deposit.minimum_amount, all_deposits))


def find_profitable_deposit_info(contributions):
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
