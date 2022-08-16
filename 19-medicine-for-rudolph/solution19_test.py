# Unit tests for day 19 of AOC 2015, Medicine for Rudolph

from solution19 import possible_replacements, replace
import unittest


class TestFunctions(unittest.TestCase):

    def test_possible_replacements(self):
        r = [('H', 'HO'), ('H', 'OH'), ('O', 'HH')]

        self.assertEqual(possible_replacements(r, 'O'), ['HH'])
        self.assertEqual(possible_replacements(r, 'H'), ['HO', 'OH'])

    def test_replace(self):
        self.assertEqual(replace('abcdef', 0, 'x', 1), 'xbcdef')
        self.assertEqual(replace('abcdef', 2, 'xy', 1), 'abxydef')
        self.assertEqual(replace('abcdef', 5, 'x', 1), 'abcdex')
        self.assertEqual(replace('abcdef', 0, 'x', 2), 'xcdef')
        self.assertEqual(replace('abcdef', 2, 'xy', 2), 'abxyef')
        self.assertEqual(replace('abcdef', 2, 'xy', 2), 'abxyef')
        self.assertEqual(replace('abcdef', 5, 'xy', 1), 'abcdexy')


if __name__ == '__main__':
    unittest.main()
