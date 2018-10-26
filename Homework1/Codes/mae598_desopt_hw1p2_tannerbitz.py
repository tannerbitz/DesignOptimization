#!/usr/bin/python3

import cvxpy as cp


x = cp.Variable(3, integer=True)

constraints = [5*x[0] + 3*x[2] >=10,
               6*x[1] + 2*x[2] >=20,
               x[0] >= 0,
               x[1] >= 0,
               x[2] >= 0]

obj = cp.Minimize(5*x[0] + 6*x[1] + 7*x[2])

# Form and solve problem.
prob = cp.Problem(obj, constraints)
prob.solve(solver='CBC')  # Returns the optimal value.
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x.value)
