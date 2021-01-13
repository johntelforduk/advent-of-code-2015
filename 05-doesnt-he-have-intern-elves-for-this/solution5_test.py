# Unit tests for day 5 of AOC 2015, Doesn't He Have Intern-Elves For This?


from solution5 import is_nice1, is_nice2
import unittest


class TestFunctions(unittest.TestCase):

    def test_functions(self):

        self.assertTrue(is_nice1('ugknbfddgicrmopn'))
        self.assertTrue(is_nice1('aaa'))
        self.assertFalse(is_nice1('jchzalrnumimnmhp'))
        self.assertFalse(is_nice1('haegwjzuvuyypxyu'))
        self.assertFalse(is_nice1('dvszwmarrgswjxmb'))

        self.assertTrue(is_nice2('qjhvhtzxzqqjkmpb'))
        self.assertTrue(is_nice2('xxyxx'))
        self.assertFalse(is_nice2('uurcxstgmygtbstg'))
        self.assertFalse(is_nice2('ieodomkazucvgmuy'))


if __name__ == '__main__':
    unittest.main()
