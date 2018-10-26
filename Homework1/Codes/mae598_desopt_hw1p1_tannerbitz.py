import numpy as np
from scipy.optimize import minimize, LinearConstraint, NonlinearConstraint

#MAE 598 Design Optimization - HW1 - Problem 1
objectivefun = lambda x: 24.55*x[0] + 26.75*x[1] + 39.00*x[2] + 40.50*x[3]

# Constraints - Linear Inequalities
def linconineq1(x):
    return 2.3*x[0] + 5.6*x[1] + 11.1*x[2] + 1.3*x[3] - 5

def linconineq2(x):
    return x[0]

def linconineq3(x):
    return x[1]

def linconineq4(x):
    return x[2]

def linconineq5(x):
    return x[3]

# Constraints - Linear Equalities
def linconeq1(x):
    return x[0] + x[1] + x[2] + x[3] -1

# Constraints - Nonlinear Inequalities
def nonlincon1(x):
    return [12*x[0] + 11.9*x[1] + 41.8*x[2] + 52.1*x[3] - 21 -
            1.645*(0.28*x[0]**2 + 0.19*x[1]**2 + 20.5*x[2]**2 + 0.62*x[3]**2)**(1/2)]

cons = ([{'type': 'ineq', 'fun': linconineq1},
         {'type': 'ineq', 'fun': linconineq2},
         {'type': 'ineq', 'fun': linconineq3},
         {'type': 'ineq', 'fun': linconineq4},
         {'type': 'ineq', 'fun': linconineq5},
         {'type': 'eq'  , 'fun': linconeq1  },
         {'type': 'ineq', 'fun': nonlincon1 }])

#Initial condition
initX = np.array([1, 1, 1, 1])

# Perform Optimization
res = minimize(fun=objectivefun, x0=initX, constraints=cons)

# Format and print result
resstring = "{:3.4f}".format(res.x[0])
for i in range(1, len(res.x)):
    resstring += " {:3.4f}".format( float(res.x[i]))

print("The solution to the optimization was: ")
print(resstring)