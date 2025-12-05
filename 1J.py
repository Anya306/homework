import unittest
import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd

'''
def mn(n):
    if not isinstance(n, int):
        raise TypeError("Input int")
    if n <= 0:
        raise ValueError("Input value > 0")

    mas = []
    i = 2
    while n > 1:
        if n % i == 0:
            mas.append(i)
            n = n // i
            i = 2
        else:
            i += 1
    return mas


class TestPrimeFactors(unittest.TestCase):
    def test_output(self):
        self.assertEqual(mn(12), [2, 2, 3])
        self.assertEqual(mn(1), [])
        self.assertEqual(mn(33), [3, 11])

    def test_intput_is_int(self):
        with self.assertRaises(TypeError):
            mn("12")
        with self.assertRaises(TypeError):
            mn(3.14)
        with self.assertRaises(TypeError):
            mn(None)

    def test_value(self):
        with self.assertRaises(ValueError):
            mn(0)
        with self.assertRaises(ValueError):
            mn(-5)
# задача 1
'''

'''
def line_coefficient(x, y):
    x = np.array(x)
    y = np.array(y)
    if x.size == 0:
        raise ValueError
    if np.all(x == x[0]):
        raise ValueError
    a, b = np.polyfit(x, y, 1)
    return a, b


class TestLinearRegression(unittest.TestCase):

    def test_line1(self):
        x1 = [1, 2, 3, 4]
        y1 = [2, 4, 6, 8]
        a, b = line_coefficient(x1, y1)
        self.assertAlmostEqual(a, 2.0, places=5)
        self.assertAlmostEqual(b, 0.0, places=5)

    def test_line2(self):
        x1 = [0, 1, 2]
        y1 = [1, 3, 5]
        a, b = line_coefficient(x1, y1)
        self.assertAlmostEqual(a, 2.0, places=5)
        self.assertAlmostEqual(b, 1.0, places=5)

    def test_point(self):
        x1 = [5]
        y1 = [10]
        a, b = line_coefficient(x1, y1)
        self.assertAlmostEqual(a, 0.0, places=5)
        self.assertAlmostEqual(b, 10.0, places=5)

    def test_line3(self):
        x1 = [1, 1, 1]
        y1 = [2, 3, 4]
        with self.assertRaises(ValueError):
            line_coefficient(x1, y1)

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            line_coefficient([], [])
# задача 2
'''

'''
def quicksort(arr):
    if not isinstance(arr, (list, tuple)):
        raise TypeError
    for item in arr:
        if not isinstance(item, (int, float)):
            raise TypeError

    if len(arr) <= 1:
        return list(arr)

    p = arr[len(arr) // 2]
    l = [x for x in arr if x < p]
    m = [x for x in arr if x == p]
    r = [x for x in arr if x > p]
    return quicksort(l) + m + quicksort(r)


class TestQuicksort(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(quicksort([]), [])
        self.assertEqual(quicksort([5]), [5])
        self.assertEqual(quicksort([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])

    def test_sorted_and_reverse(self):
        self.assertEqual(quicksort([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(quicksort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_with_duplicates(self):
        self.assertEqual(quicksort([2, 2, 2]), [2, 2, 2])

    def test_negative_numbers(self):
        self.assertEqual(quicksort([-3, -1, -2]), [-3, -2, -1])

    def test_invalid_type_input(self):
        with self.assertRaises(TypeError):
            quicksort("hello")
        with self.assertRaises(TypeError):
            quicksort(42)

    def test_invalid_element_type(self):
        with self.assertRaises(TypeError):
            quicksort([1, 2, "three"])
        with self.assertRaises(TypeError):
            quicksort([1, None, 3])
# задача 3
'''

if __name__ == "__main__":
    unittest.main()
