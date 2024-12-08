from unittest import TestCase, main


def reverse_word(word: str):
    return word[::-1]


def divide(a, b):
    """

    Args:
        a (int | float): _description_
        b (int | float): _description_

    Returns:
        _type_: float
    """
    return a / b


class TestReverseWord(TestCase):
    def test_correct_reverse(self):
        self.assertEqual(reverse_word("abcde"), "edcba")

    def test_almost_equal_value(self):
        self.assertAlmostEqual(divide(22, 7), 3.14, places=2)

    def test_raises_error(self):
        with self.assertRaises(ZeroDivisionError) as err:
            divide(2, 0)
        self.assertEqual(str(err.exception), "division by zero")


if __name__ == "__main__":
    main()
