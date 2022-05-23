import unittest

from bot.business_logic.search_utils.find_best_contribution_from_all import find_best_contribution_from_all
from test.business_logic_test import create_test_data


class FindBestContributionFromAllTest(unittest.TestCase):
    def test_find_best_contribution_from_all(self):
        test_cases = create_test_data.get_test_user_input_case1()
        contribution_dict = create_test_data.get_test_dict_case1()
        for test in test_cases:
            self.find_best_contribution_from_all(contribution_dict, test,
                                                 create_test_data.create_test_contribution
                                                 (15, 1000, 12, "Bank2", "Contribution2", 0),)

    def find_best_contribution_from_all(self, contribution_dict, user_input, expected_contribution):
        user_output = find_best_contribution_from_all(contribution_dict, user_input)
        actual_contribution = user_output.get_contribution()
        self.assertTrue(expected_contribution.equals(actual_contribution))


if __name__ == '__main__':
    unittest.main()
