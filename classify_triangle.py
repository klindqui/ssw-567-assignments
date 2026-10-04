
"""Classify triangles by their side lengths and test the results."""

import unittest


def classify_triangle(a, b, c):
    """Determine the triangle type and whether it is a right triangle."""
    right = False
    triangle_type = ""

    if a + b > c and a + c > b and b + c > a:
        pass
    else:
        return "Not a triangle, Right: False"

    if a <= 0 or b <= 0 or c <= 0:
        return "Not a triangle, Right: False"

    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        right = True

    if a == b and b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    return f"{triangle_type}, Right: {right}"


def run_classify_triangle(a, b, c):
    """Print the classification of a triangle."""
    result = classify_triangle(a, b, c)
    print(f"Triangle with sides {a}, {b}, {c} is classified as: {result}")


class TestTriangles(unittest.TestCase):
    """Test the triangle classification function."""

    def test_equilateral(self):
        """Test an equilateral triangle."""
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral, Right: False")

    def test_isosceles(self):
        """Test an isosceles triangle."""
        self.assertEqual(classify_triangle(3, 3, 4), "Isosceles, Right: False")

    def test_scalene(self):
        """Test a right scalene triangle."""
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene, Right: True")

    def test_negatives_and_zeroes(self):
        """Test invalid side lengths."""
        self.assertEqual(classify_triangle(-1, 0, 3), "Not a triangle, Right: False")

    def test_not_a_triangle(self):
        """Test sides that cannot form a triangle."""
        self.assertEqual(classify_triangle(1, 2, 3), "Not a triangle, Right: False")

    def test_isosceles_different_order(self):
        """Test an isosceles triangle with reordered sides."""
        self.assertEqual(classify_triangle(3, 4, 3), "Isosceles, Right: False")

    def test_right_different_order(self):
        """Test a right triangle with reordered sides."""
        self.assertEqual(classify_triangle(5, 3, 4), "Scalene, Right: True")

    def test_scalene_not_right(self):
        """Test a scalene triangle that is not right."""
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene, Right: False")


if __name__ == "__main__":
    run_classify_triangle(3, 4, 5)
    run_classify_triangle(3, 3, 3)

    unittest.main(exit=False)
