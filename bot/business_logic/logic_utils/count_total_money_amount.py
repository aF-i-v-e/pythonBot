def count_contribution_total_money_amount(user_input, contribution):
    """Вычисление итоговой суммы денег, которую получит пользователь в конце срока вклада с учетом того,
    что вклад может подразумевать покупку пакета услуг

        Аргументы:

        user_input: Входные данные пользователя

        contribution: Вклад
        """
    total_money_amount = count_total_money_amount_bank(user_input.get_amount(), contribution.get_percent(),
                                                       contribution.get_months_number())
    return total_money_amount - contribution.get_package_services_price()


def count_total_money_amount_bank(start_sum, percent, months_number):
    """Вычисление суммы денег, которую можно получить по вкладу

    Аргументы:

    start_sum: Начальная сумма клада.

    percent: Процент, который начисляется каждый месяц на сумму вклада.

    months_number: Срок действия вклада.
    """
    return ((1 + percent / 100) ** months_number) * start_sum
