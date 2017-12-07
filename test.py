from main import LotteryNumberValidator

import unittest


class TestLotteryNumberValidator(unittest.TestCase):
    def test_small_string(self):
        small_string = '123'
        lottery_validator = LotteryNumberValidator([small_string])
        self.assertEqual(lottery_validator.fetch_string_mappings()[small_string], None)

    def test_huge_string(self):
        huge_string = '122345678901234567890'
        lottery_validator = LotteryNumberValidator([huge_string])
        self.assertEqual(lottery_validator.fetch_string_mappings()[huge_string], None)

    def test_invalid_number_input_string(self):
        invalid_number_input_string = '01234567'
        lottery_validator = LotteryNumberValidator([invalid_number_input_string])
        self.assertEqual(lottery_validator.fetch_string_mappings()[invalid_number_input_string], None)

    def test_all_one_digit_valid_string(self):
        one_digit_valid_string = '1234567'
        valid_formatting = '1 2 3 4 5 6 7'
        lottery_validator = LotteryNumberValidator([one_digit_valid_string])
        self.assertEqual(lottery_validator.fetch_string_mappings()[one_digit_valid_string], valid_formatting)

    def test_all_two_digit_valid_string(self):
        two_digit_valid_string = '11223344551617'
        valid_formatting = '11 22 33 44 55 16 17'
        lottery_validator = LotteryNumberValidator([two_digit_valid_string])
        self.assertEqual(lottery_validator.fetch_string_mappings()[two_digit_valid_string], valid_formatting)

    def test_mixed_digits_valid_string(self):
        mixed_digit_valid_string = '1122334455161'
        valid_formatting = '11 22 33 44 55 16 1'
        lottery_validator = LotteryNumberValidator([mixed_digit_valid_string])
        self.assertEqual(lottery_validator.fetch_string_mappings()[mixed_digit_valid_string], valid_formatting)

    def test_multiple_strings(self):
        first_string = '1122334455161'
        second_string = '1234567'
        valid_first = '11 22 33 44 55 16 1'
        valid_second = '1 2 3 4 5 6 7'
        lottery_validator = LotteryNumberValidator([first_string, second_string])
        self.assertEqual(lottery_validator.fetch_string_mappings()[first_string], valid_first)
        self.assertEqual(lottery_validator.fetch_string_mappings()[second_string], valid_second)


if __name__ == '__main__':
    unittest.main()
