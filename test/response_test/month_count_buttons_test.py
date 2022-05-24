import unittest

from bot.response.month_count_buttons_info import get_month_count_list
from test.business_logic_test.create_test_data import get_test_contributions_case1, get_test_month_count_list_case1


class MonthCountButtonsTest(unittest.TestCase):
    def test_month_count_buttons(self):
        contributions = get_test_contributions_case1()
        expected_list = get_test_month_count_list_case1()
        self.assert_equals(contributions, expected_list)

    def assert_equals(self, contributions, expected_list):
        actual_list = get_month_count_list(contributions)
        self.assertTrue(actual_list == expected_list)
