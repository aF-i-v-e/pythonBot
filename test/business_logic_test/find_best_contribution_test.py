import unittest
import create_test_data
from bot.business_logic.find_best_contribution import find_best_contribution


class FidBestContributionTest(unittest.TestCase):
    def test_find_best_contribution(self):
        test_cases = [
            [
                create_test_data.create_test_user_input(1500, 9),
                create_test_data.create_test_contribution(8, 1000, 9, "Bank1", "Contribution2", 0),
            ],
            [
                create_test_data.create_test_user_input(100, 9),
                None,
            ],
            [
                create_test_data.create_test_user_input(143000, 12),
                create_test_data.create_test_contribution(15, 1000, 12, "Bank2", "Contribution2", 0),
            ],
            [
                create_test_data.create_test_user_input(14700, 7),
                None
            ],
            [
                create_test_data.create_test_user_input(25000, 7),
                create_test_data.create_test_contribution(4.85, 20000, 7, "Bank3", "Contribution1", 0),
            ],
            [
                create_test_data.create_test_user_input(56000, 8),
                None
            ],
            [
                create_test_data.create_test_user_input(56478, 0),
                create_test_data.create_test_contribution(15, 1000, 12, "Bank2", "Contribution2", 0)
            ],
        ]
        contributions = create_test_data.get_test_contributions_case1()
        for test in test_cases:
            self.find_best_contribution(contributions, test[0], test[1])

    def find_best_contribution(self, contributions, user_input, expected_contribution):
        user_output = find_best_contribution(contributions, user_input)
        if expected_contribution is None and user_output is None:
            self.assertTrue(True)
        else:
            actual_contribution = user_output.get_contribution()
            self.assertTrue(expected_contribution.equals(actual_contribution))


if __name__ == '__main__':
    unittest.main()
