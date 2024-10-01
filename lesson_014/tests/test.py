import unittest
from random import randint

from lesson_014.bowling import get_score


class BowlingTest(unittest.TestCase):
    def test_feedback(self):
        test = ''
        self.assertIsNotNone(get_score(game_result=test))
    def test_huge_numbers(self):
        test = ''
        for _ in range(1, 1000):
            _appropriate_vals = ['X', str(randint(0,9))+'/', str(randint(0,9))*2]
            test += _appropriate_vals[randint(0,2)]
        result = get_score(game_result=test)
        self.assertGreater(result, 0)

    def test_incorrect_values(self):
        test = ''
        for _ in range(1, 1000):
            _appropriate_vals = ['x', str(randint(0, 9)) + "!", str(randint(0, 9)) * 4]
            test += _appropriate_vals[randint(0, 2)]
        with self.assertWarns(SyntaxWarning):
            get_score(game_result=test)



if __name__ == '__main__':
    unittest.main()
