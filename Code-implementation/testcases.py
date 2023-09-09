import unittest

class TestCSVProcessing(unittest.TestCase):

    def test_is_armstrong(self):
        self.assertTrue(is_armstrong(153))  # 153 is an Armstrong number
        self.assertFalse(is_armstrong(370))  # 370 is not an Armstrong number
        self.assertFalse(is_armstrong(371))  # 371 is not an Armstrong number

    def test_is_strong(self):
        self.assertTrue(is_strong(145))  # 145 is a Strong number
        self.assertFalse(is_strong(123))  # 123 is not a Strong number
        self.assertTrue(is_strong(40585))  # 40585 is a Strong number

    def test_is_perfect(self):
        self.assertTrue(is_perfect(28))  # 28 is a Perfect number
        self.assertFalse(is_perfect(6))  # 6 is not a Perfect number
        self.assertTrue(is_perfect(496))  # 496 is a Perfect number

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
