Feature: Quadratic Equation Solver

  Scenario: Valid input that has two distinct real solutions
    Given I have coefficients 1, -3, 2
    When I solve the equation
    Then I should get roots [1.0, 2.0]

  Scenario: Valid input that has one real solution
    Given I have coefficients 1, 2, 1
    When I solve the equation
    Then I should get roots [-1.0 ]

  Scenario: Invalid input that has no real solution
    Given I have coefficients 1, 0, 1
    When I solve the equation
    Then I should not have any real roots