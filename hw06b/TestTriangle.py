
import unittest
from Triangle import classifyTriangle


class TestTriangles(unittest.TestCase):

    # Right triangle tests
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(4, 5, 3), 'Right')

    def testRightTriangleLarge(self):
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right')

    # Equilateral triangle tests
    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral')

    def testEquilateralLarge(self):
        self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral')

    # Isosceles triangle tests
    def testIsoscelesA(self):
        self.assertEqual(classifyTriangle(5, 5, 3), 'Isoceles')

    def testIsoscelesB(self):
        self.assertEqual(classifyTriangle(5, 3, 5), 'Isoceles')

    def testIsoscelesC(self):
        self.assertEqual(classifyTriangle(3, 5, 5), 'Isoceles')

    # Scalene triangle tests
    def testScaleneA(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene')

    def testScaleneB(self):
        self.assertEqual(classifyTriangle(7, 8, 9), 'Scalene')

    # Invalid triangle tests
    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(1, 1, 3), 'NotATriangle')

    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(10, 2, 3), 'NotATriangle')

    # Invalid input tests
    def testZeroSide(self):
        self.assertEqual(classifyTriangle(0, 4, 5), 'InvalidInput')

    def testNegativeSide(self):
        self.assertEqual(classifyTriangle(-1, 4, 5), 'InvalidInput')

    def testAboveMaximum(self):
        self.assertEqual(classifyTriangle(201, 4, 5), 'InvalidInput')

    def testAllAboveMaximum(self):
        self.assertEqual(classifyTriangle(201, 202, 203), 'InvalidInput')

    def testFloatInput(self):
        self.assertEqual(classifyTriangle(3.5, 4, 5), 'InvalidInput')

    def testStringInput(self):
        self.assertEqual(classifyTriangle("3", 4, 5), 'InvalidInput')

    def testAllZero(self):
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

