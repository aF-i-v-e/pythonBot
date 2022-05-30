import unittest

from bot.business_logic.logic_utils.count_total_money_amount import count_contribution_total_money_amount, \
    count_total_money_amount_bank
from test.business_logic_test import create_test_data


class TotalMoneyAmountTest(unittest.TestCase):

    def test_total_money_amount_cases(self):
        test_cases = [
            [1000, 8, 9,  1061.63],
            [42364578, 15, 12, 49174875.30],
            [0, 20, 3, 0],
            [60000, 4.85, 7,  61718.22]
        ]
        for test in test_cases:
            self.count_total_money_amount_bank(test[0], test[1], test[2], test[3])

    def test_contribution_total_money_amount_cases(self):
        test_cases = [
            [
                create_test_data.create_test_user_input(1000, 9),
                create_test_data.create_test_contribution(8, 1000, 9, "Bank1", "Contribution1", 50),
                1011.63
            ],
            [
                create_test_data.create_test_user_input(1000, 9),
                create_test_data.create_test_contribution(8, 1000, 9, "Bank1", "Contribution2", 0),
                1061.63
            ],

            [
                create_test_data.create_test_user_input(42364578, 12),
                create_test_data.create_test_contribution(15, 1000, 12, "Bank2", "Contribution1", 50),
                49174825.30
            ],
            [
                create_test_data.create_test_user_input(42364578, 12),
                create_test_data.create_test_contribution(15, 1000, 12, "Bank2", "Contribution2", 0),
                49174875.30
            ],

            [
                create_test_data.create_test_user_input(60000, 7),
                create_test_data.create_test_contribution(4.85, 20000, 7, "Bank3", "Contribution1", 100),
                61618.22
            ],
            [
                create_test_data.create_test_user_input(60000, 7),
                create_test_data.create_test_contribution(4.85, 20000, 7, "Bank3", "Contribution1", 0),
                61718.22
            ]
        ]
        for test in test_cases:
            self.count_contribution_total_money_amount(test[0], test[1], test[2])

    def count_contribution_total_money_amount(self, user_input, contribution, expected_amount):
        actual_amount = count_contribution_total_money_amount(user_input, contribution)
        self.assertEqual(expected_amount, actual_amount)

    def count_total_money_amount_bank(self, start_sum, percent, months_number, expected_amount):
        actual_amount = count_total_money_amount_bank(start_sum, percent, months_number)
        self.assertEqual(expected_amount, actual_amount)


if __name__ == '__main__':
    unittest.main()
