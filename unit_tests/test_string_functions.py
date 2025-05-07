from unittest import TestCase

from .string_functions import *

class StringTests(TestCase):
    def test_greeting_jeremy(self):
        """Test for greet_by_name"""
        # Step 1: Choose a scenario - here I'm choosing name='Jeremy'

        # Step 2: Decide what the expected outcome is for the scenario
        expected = 'Hello, Jeremy!'

        # Step 3: Call the function being tested to get its actual output
        actual = greet_by_name('Jeremy')

        # Step 4: Compare expected & actual outcomes. If they match, the test 
        # passes
        self.assertEqual(actual, expected)

    def test_greeting_ceina(self):
        """Test for greet_by_name"""
        expected = 'Hello, Ceina!'
        actual = greet_by_name('Ceina')
        self.assertEqual(actual, expected)

    def test_reverse_long(self):
        """Test reversing a long string."""
        expected = 'gnitsetksalf'
        actual = reverse('flasktesting')
        self.assertEqual(actual, expected)

    def test_reverse_short(self):
        """Test reversing a short string."""
        expected = 'yeh'
        actual = reverse('hey')
        self.assertEqual(actual, expected)

    def test_reverse_words_long(self):
        """Test reversing words in a long string."""
        expected = 'lab testing flask'
        actual = reverse_words('flask testing lab')
        self.assertEqual(actual, expected)

    def test_reverse_words_short(self):
        """Test reversing words in a short string."""
        expected = 'there hi'
        actual = reverse_words('hi there')
        self.assertEqual(actual, expected)

    def test_sarcastic_long(self):
        """Test sarcastic-ifying a long string."""
        expected = 'fLaSkTeStInGlAb'
        actual = sarcastic('flasktestinglab')
        self.assertEqual(actual, expected)

    def test_sarcastic_short(self):
        """Test sarcastic-ifying a short string."""
        expected = 'bRyAn'
        actual = sarcastic('bryan')
        self.assertEqual(actual, expected)


    def test_find_longest_word_empty(self):
        """Test finding the longest word in an empty string."""
        expected = ''
        actual = find_longest_word('')
        self.assertEqual(actual, expected)
