import unittest


def multiply(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("")
    return round(a * b, 2)

class TestMultiply(unittest.TestCase):
    def test_multiply_1_and_2(self):
        self.assertEqual(multiply(1,2), 2)

    def test_multiply_10_1_and_2_3(self):
        self.assertAlmostEqual(multiply(10.1567,2.3),23.36, places=2)

    def test_multiply_errortype(self):
        with self.assertRaises(TypeError):
            multiply('str',2)

if __name__ == '__main__':
    unittest.main()