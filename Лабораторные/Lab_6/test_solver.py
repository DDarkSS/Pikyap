import unittest
from B2_Solver import QuadraticEquationSolver  # Импортируйте ваш класс

class TestQuadraticEquationSolver(unittest.TestCase):
    def test_is_digit(self):
        self.assertTrue(QuadraticEquationSolver.is_digit("123"))
        self.assertTrue(QuadraticEquationSolver.is_digit("123.456"))
        self.assertFalse(QuadraticEquationSolver.is_digit("abc"))
        self.assertFalse(QuadraticEquationSolver.is_digit("123abc"))

    def test_input_check(self):
        self.assertTrue(QuadraticEquationSolver.input_check(["1", "2", "3"]))
        self.assertFalse(QuadraticEquationSolver.input_check(["1", "two", "3"]))
        self.assertFalse(QuadraticEquationSolver.input_check(["1"]))
        self.assertFalse(QuadraticEquationSolver.input_check([]))

    def test_solve_b2_equation(self):
        self.assertEqual(QuadraticEquationSolver.solve_b2_equation(1, -3, 2), [1.0, 2.0])
        self.assertEqual(QuadraticEquationSolver.solve_b2_equation(1, 2, 1), [-1.0])
        self.assertFalse(QuadraticEquationSolver.solve_b2_equation(1, 0, 1))

if __name__ == '__main__':
    unittest.main()