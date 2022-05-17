import unittest

from bot.business_logic.logic_utils.count_total_money_amount import count_contribution_total_money_amount, \
    count_total_money_amount_bank
from test.business_logic_test import create_test_data


class TotalMoneyAmountTest(unittest.TestCase):

    def test_total_money_amount_cases(self):
        test_cases = [
            [1000, 8, 9, 1999.00],
            [42364578, 15, 12, 226661087.91],
            [0, 20, 3, 0],
            [60000, 4.85, 7, 83585.37]
        ]
        for test in test_cases:
            self.count_total_money_amount_bank(test[0], test[1], test[2], test[3])

    def test_contribution_total_money_amount_cases(self):
        test_cases = [
            [
                create_test_data.create_test_user_input(1000, 9),
                create_test_data.create_test_contribution(8, 1000, 9, "Bank1", "Contribution1", 500),
                1499.00
            ],
            [
                create_test_data.create_test_user_input(1000, 9),
                create_test_data.create_test_contribution(8, 1000, 9, "Bank1", "Contribution2", 0),
                1999.00
            ],

            [
                create_test_data.create_test_user_input(42364578, 12),
                create_test_data.create_test_contribution(15, 1000, 12, "Bank2", "Contribution1", 2300),
                226658787.91
            ],
            [
                create_test_data.create_test_user_input(42364578, 12),
                create_test_data.create_test_contribution(15, 1000, 12, "Bank2", "Contribution2", 0),
                226661087.91
            ],

            [
                create_test_data.create_test_user_input(60000, 7),
                create_test_data.create_test_contribution(4.85, 20000, 7, "Bank3", "Contribution1", 1000),
                82585.37
            ],
            [
                create_test_data.create_test_user_input(60000, 7),
                create_test_data.create_test_contribution(4.85, 20000, 7, "Bank3", "Contribution1", 0),
                83585.37
            ]
        ]
        for test in test_cases:
            self.count_contribution_total_money_amount(test[0], test[1], test[2])

    def count_contribution_total_money_amount(self, user_input, contribution, expected_amount):
        actual_amount = count_contribution_total_money_amount(user_input, contribution)
        self.assertEqual(expected_amount, round(actual_amount, 2))

    def count_total_money_amount_bank(self, start_sum, percent, months_number, expected_amount):
        actual_amount = count_total_money_amount_bank(start_sum, percent, months_number)
        self.assertEqual(expected_amount, round(actual_amount, 2))


if __name__ == '__main__':
    unittest.main()
