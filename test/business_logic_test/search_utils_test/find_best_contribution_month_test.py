import unittest

from bot.business_logic.search_utils.find_best_contribution_month import find_best_contribution_month
from test.business_logic_test import create_test_data


class FindBestContributionMonthTest(unittest.TestCase):
    def test_find_best_contribution_month(self):
        test_cases = [
            [
                create_test_data.create_test_user_input(1500, 9),
                create_test_data.create_test_contribution(8, 1000, 9, "Bank1", "Contribution2", 0),
            ],
            [
                create_test_data.create_test_user_input(143000, 12),
                create_test_data.create_test_contribution(15, 1000, 12, "Bank2", "Contribution2", 0),
            ],
            [
                create_test_data.create_test_user_input(25000, 7),
                create_test_data.create_test_contribution(4.85, 20000, 7, "Bank3", "Contribution1", 0),
            ]
        ]
        contribution_dict = create_test_data.get_test_dict_case1()
        for test in test_cases:
            self.find_best_contribution_month(contribution_dict, test[0], test[1])

    def find_best_contribution_month(self, contribution_dict, user_input, expected_contribution):
        user_output = find_best_contribution_month(contribution_dict, user_input)
        actual_contribution = user_output.get_contribution()
        self.assertTrue(expected_contribution.equals(actual_contribution))


if __name__ == '__main__':
    unittest.main()
