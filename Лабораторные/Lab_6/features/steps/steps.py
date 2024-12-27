from behave import given, when, then
from B2_Solver import QuadraticEquationSolver

@given('I have coefficients {A:d}, {B:d}, {C:d}')
def step_impl(context, A, B, C):
    context.coefficients = (A, B, C)

@when('I solve the equation')
def step_impl(context):
    A, B, C = context.coefficients
    context.roots = QuadraticEquationSolver.solve_b2_equation(A, B, C)

@then('I should get roots {expected_roots}')
def step_impl(context, expected_roots):
    expected_roots = eval(expected_roots)  # Преобразуем строку в список
    assert context.roots == expected_roots

@then('I should not have any real roots')
def step_impl(context):
    assert context.roots is False