"""Unit tests for the adapted engine."""

import unittest

from micrograd_lab import Value


class TestValue(unittest.TestCase):
    def test_arithmetic(self) -> None:
        a = Value(2)
        b = Value(3)
        self.assertEqual((a + b).data, 5)
        self.assertEqual((a * b).data, 6)
        self.assertEqual((a - b).data, -1)
        self.assertEqual((3 - a).data, 1)
        self.assertAlmostEqual((b / a).data, 1.5)
        self.assertEqual((6 / b).data, 2)
        self.assertEqual((a**3).data, 8)
        self.assertEqual((a + 4).data, 6)
        self.assertEqual((4 + a).data, 6)
        self.assertEqual((4 * a).data, 8)

    def test_gradients(self) -> None:
        a = Value(2)
        b = Value(-3)
        result = a * b + a**2
        result.backward()
        self.assertAlmostEqual(a.grad, 1)
        self.assertAlmostEqual(b.grad, 2)

    def test_relu(self) -> None:
        positive = Value(3)
        positive.relu().backward()
        self.assertEqual(positive.grad, 1)
        negative = Value(-2)
        negative.relu().backward()
        self.assertEqual(negative.grad, 0)

    def test_invalid_power(self) -> None:
        with self.assertRaises(TypeError):
            Value(2).__pow__("wrong")  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
