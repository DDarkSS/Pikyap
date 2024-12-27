class QuadraticEquationSolver:
    @staticmethod
    def is_digit(string):
        if string.isdigit():
            return True
        else:
            try:
                float(string)
                return True
            except ValueError:
                return False

    @staticmethod
    def input_check(sp):
        if len(sp) != 3:
            return False
        for i in range(3):
            if not QuadraticEquationSolver.is_digit(sp[i]):
                return False
        return True

    @staticmethod
    def discr_search(A, B, C):
        return B * B - 4 * A * C

    @staticmethod
    def result_search(A, B, D):
        res1 = (-B + D ** 0.5) / (2 * A)
        res2 = (-B - D ** 0.5) / (2 * A)
        return {res1, res2}

    @staticmethod
    def solve_b2_equation(A, B, C):
        D = QuadraticEquationSolver.discr_search(A, B, C)
        if D < 0:
            return False
        else:
            return sorted(QuadraticEquationSolver.result_search(A, B, D))

    @staticmethod
    def check(A, B, C, x):
        return A * x * x + B * x + C