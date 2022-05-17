import unittest

from bot.business_logic.logic_utils.divide_contributions import divide_contributions, identify_suitable_contributions
from test.business_logic_test import create_test_data


class DivideContributionsTests(unittest.TestCase):
    def test_divide_contributions(self):
        test_contributions = create_test_data.get_test_contributions_case1()
        expected_dict = create_test_data.get_test_dict_case1()
        self.divide_contributions(test_contributions, expected_dict)

    def test_identify_suitable_contributions(self):
        test_contributions = create_test_data.get_test_contributions_case1()
        test_cases = [
            [
                test_contributions,
                5000,
                [test_contributions[0], test_contributions[1],
                 test_contributions[2], test_contributions[3]]
            ],
            [
                test_contributions,
                1000,
                [test_contributions[0], test_contributions[1],
                 test_contributions[2], test_contributions[3]]
            ],
            [
                test_contributions,
                500,
                []
            ],
            [
                test_contributions,
                38567,
                test_contributions
            ],
            [
                test_contributions,
                20000,
                test_contributions
            ],
            [
                test_contributions,
                15123,
                [test_contributions[0], test_contributions[1],
                 test_contributions[2], test_contributions[3]]
            ],
        ]
        for test in test_cases:
            self.identify_suitable_contributions(test[0], test[1], test[2])

    def divide_contributions(self, test_contributions, expected_dict):
        actual_dict = divide_contributions(test_contributions)
        self.assertTrue(self.compare_dictionaries(expected_dict, actual_dict))

    def compare_dictionaries(self, expected_dict, actual_dict):
        for key in expected_dict:
            expected_value = expected_dict[key]
            if key in actual_dict:
                actual_value = actual_dict[key]
                same_content = self.compare_arrays(expected_value, actual_value)
                if not same_content:
                    print("Dictionaries are not equal!")
                    return False
            else:
                print(f"Key {key} doesn't exist in actual dictionary!")
                return False
        return True

    def compare_arrays(self, first_array, second_array):
        flag = False
        first_length = len(first_array)
        second_length = len(second_array)
        if first_length != second_length:
            print(f"Arrays don't have the same length! First array length = {first_length} "
                  f"and the second array length {second_length}!")
            return False
        for contribution1 in first_array:
            for contribution2 in second_array:
                if contribution1.equals(contribution2):
                    flag = True
            if not flag:
                print("Arrays are not equal. The element from the first array is not contained "
                      "in the second array!")
                return False
        return True

    def identify_suitable_contributions(self, all_contributions, user_amount, expected_contributions):
        actual_deposits = identify_suitable_contributions(all_contributions, user_amount)
        self.assertEqual(expected_contributions, actual_deposits)


if __name__ == '__main__':
    unittest.main()
