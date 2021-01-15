# Unit tests for day 6 of AOC 2015, Probably a Fire Hazard.


from solution6_1 import parse_instruction
import unittest


class TestFunctions(unittest.TestCase):

    def test_functions(self):

        self.assertEqual(parse_instruction('turn off 660,55 through 986,197'), ('off', 660, 55, 986, 197))
        self.assertEqual(parse_instruction('turn on 226,196 through 599,390'), ('on', 226, 196, 599, 390))
        self.assertEqual(parse_instruction('toggle 322,558 through 977,958'), ('toggle', 322, 558, 977, 958))



if __name__ == '__main__':
    unittest.main()
