import unittest

def classify_triangle(a, b, c):
    right = False
    triangle_type = ""

    if a + b > c and a + c > b and b + c > a:
        pass
    else:
        return "Not a triangle, Right: False"
    
    if a <= 0 or b <= 0 or c <= 0:
        return  "Not a triangle, Right: False"

    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        right = True
    
    if a == b and b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"
  

    return f"{triangle_type}, Right: {right}"

def runClassifyTriangle(a, b, c):
    result = classify_triangle(a, b, c)
    print(f"Triangle with sides {a}, {b}, {c} is classified as: {result}")

class TestTriangles(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), ("Equilateral, Right: False"))

    def test_isosceles(self):
        self.assertEqual(classify_triangle(3, 3, 4), ("Isosceles, Right: False"))

    def test_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 5), ("Scalene, Right: True"))

    def test_negatives_and_zeroes(self):
        self.assertEqual(classify_triangle(-1, 0, 3), ( "Not a triangle, Right: False"))

    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), ( "Not a triangle, Right: False"))

    def test_isosceles_different_order(self):
        self.assertEqual(classify_triangle(3, 4, 3), ("Isosceles, Right: False"))

    def test_right_different_order(self):
        self.assertEqual(classify_triangle(5, 3, 4), ("Scalene, Right: True"))

    def test_scalene_not_right(self):
        self.assertEqual(classify_triangle(4, 5, 6), ("Scalene, Right: False"))


if __name__ == "__main__":
    runClassifyTriangle(3, 4, 5)
    runClassifyTriangle(3, 3, 3)

    unittest.main(exit=False)