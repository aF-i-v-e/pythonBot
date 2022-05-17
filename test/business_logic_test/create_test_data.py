from bot.api.user_input import UserInput
from bot.data.contribution import Contribution


def create_test_user_input(amount, month_count):
    return UserInput("TestName", amount, month_count)


def create_test_contribution(percent, start_sum, month_number, bank_name, contribution_name,
                             package_services_price):
    return Contribution(percent, start_sum, month_number, bank_name, contribution_name, package_services_price)


def get_test_contributions_case1():
    return [
        create_test_contribution(8, 1000, 9, "Bank1", "Contribution1", 500),
        create_test_contribution(8, 1000, 9, "Bank1", "Contribution2", 0),
        create_test_contribution(15, 1000, 12, "Bank2", "Contribution1", 2300),
        create_test_contribution(15, 1000, 12, "Bank2", "Contribution2", 0),
        create_test_contribution(4.85, 20000, 7, "Bank3", "Contribution1", 1000),
        create_test_contribution(4.85, 20000, 7, "Bank3", "Contribution1", 0)
    ]


def get_test_user_input_case1():
    return [
        create_test_user_input(1500, 0),
        create_test_user_input(100, 9),
        create_test_user_input(143000, 0),
        create_test_user_input(14700, 0),
        create_test_user_input(25000, 0),
    ]


def get_test_dict_case1():
    test_contributions = get_test_contributions_case1()
    return {
        9: [test_contributions[0], test_contributions[1]],
        12: [test_contributions[2], test_contributions[3]],
        7: [test_contributions[4], test_contributions[5]]
    }
