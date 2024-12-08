from unittest import TestCase, main


def celsius_to_fahrenheit(celsius: float):
    return (9 / 5) * celsius + 32


class TestTemperatureChange(TestCase):
    def setUp(self) -> None:
        # This method runs before each test case inside of this test class
        self.celsius = 37

    def tearDown(self) -> None:
        # This method runs after each test case inside of this test class
        del self.celsius

    @classmethod
    def setUpClass(cls) -> None:
        # This method runs once before test case inside of this test class start
        cls.initial_value = 0

    def test_conversion_from_setup_class(self):
        self.assertEqual(self.initial_value, 0)

    def test_conversion_from_setup(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(self.celsius), 98.6)


if __name__ == "__main__":
    main()
