import unittest
import animal_divider_service


class AnimalDividerServiceTests(unittest.TestCase):
    def test_is_key_in_blacklist_valid_input(self):
        result = animal_divider_service.is_key_in_blacklist('Buffalo')
        self.assertEqual(result, False)

    def test_is_key_in_blacklist_bracket_input(self):
        result = animal_divider_service.is_key_in_blacklist('(Buffalo)')
        self.assertEqual(result, True)

    def test_is_key_in_blacklist_unallow_word_input(self):
        result = animal_divider_service.is_key_in_blacklist('of')
        self.assertEqual(result, True)

    def test_generate_other_keys_statement(self):
        result = animal_divider_service.generate_other_keys_statement(['King', 'Queen', 'Jack'], 'Jack')
        print(result)
        self.assertEqual(result, '(also King, Queen)')
