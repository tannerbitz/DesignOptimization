#!/usr/bin/python3
import numpy as np



# Antoine Equation Constants
a1_wat = 8.07131
a2_wat = 1730.63
a3_wat = 233.426

a1_dxn = 7.43155
a2_dxn = 1554.679
a3_dxn = 240.337

T = 20 # deg C


# Calc saturation pressure
def AntoineEq(a1, a2, a3, T):
    return 10**(a1 - a2/(T + a3))

psat_wat = AntoineEq(a1_wat, a2_wat, a3_wat, T)
psat_dxn = AntoineEq(a1_dxn, a2_dxn, a3_dxn, T)

# Data
x1 = np.arange(0, 1.1, 0.1)
x2 = np.ones(x1.shape) - x1
y = np.array([28.1, 34.4, 36.7, 36.9, 36.8, 36.7, 36.5, 35.4, 32.9, 27.7, 17.5])

# Objective function subfunctions
exp1inner = lambda xone, xtwo, A12, A21: A12 * (A21 * xtwo / (A12 * xone + A21 * xtwo)) ** 2
exp2inner = lambda xone, xtwo, A12, A21: A21 * (A12 * xone / (A12 * xone + A21 * xtwo)) ** 2
yerror = lambda e1inner, e2inner, xone, xtwo, y: (y - (
            xone * np.exp(e1inner) * psat_wat + xtwo * np.exp(e2inner) * psat_dxn))

# Gradient functions
dfdA12 = lambda p1, p2, x1, x2, A12, A21: p1*x1*np.exp((A12*A21**2*x2**2)/(A12*x1 + A21*x2)**2)*((A21**2*x2**2)/(A12*x1 + A21*x2)**2 - (2*A12*A21**2*x1*x2**2)/(A12*x1 + A21*x2)**3) - p2*x2*np.exp((A12**2*A21*x1**2)/(A12*x1 + A21*x2)**2)*((2*A12**2*A21*x1**3)/(A12*x1 + A21*x2)**3 - (2*A12*A21*x1**2)/(A12*x1 + A21*x2)**2)
dfdA21 = lambda p1, p2, x1, x2, A12, A21: p2*x2*np.exp((A12**2*A21*x1**2)/(A12*x1 + A21*x2)**2)*((A12**2*x1**2)/(A12*x1 + A21*x2)**2 - (2*A12**2*A21*x1**2*x2)/(A12*x1 + A21*x2)**3) - p1*x1*np.exp((A12*A21**2*x2**2)/(A12*x1 + A21*x2)**2)*((2*A12*A21**2*x2**3)/(A12*x1 + A21*x2)**3 - (2*A12*A21*x2**2)/(A12*x1 + A21*x2)**2)


# Define objective function and it's gradient xi in x:
def objfun(x):
    A12 = x[0, 0]
    A21 = x[1, 0]
    fa = np.zeros((len(x1), 1))
    for i in range(0, len(x1)):
        e1inner_i = exp1inner(x1[i], x2[i], A12, A21)
        e2inner_i = exp2inner(x1[i], x2[i], A12, A21)
        fa[i, 0] = yerror(e1inner_i, e2inner_i, x1[i], x2[i], y[i])
    return 1/2*fa.transpose().dot(fa)

def g(x):
    A12 = x[0, 0]
    A21 = x[1, 0]
    JaTrans = np.zeros((2,len(x1)))
    fa = np.zeros((len(x1), 1))
    for i in range(0, len(x1)):
        JaTrans[0, i] = dfdA12(psat_wat, psat_dxn, x1[i], x2[i], A12, A21)
        JaTrans[1, i] = dfdA21(psat_wat, psat_dxn, x1[i], x2[i], A12, A21)
        e1inner_i = exp1inner(x1[i], x2[i], A12, A21)
        e2inner_i = exp2inner(x1[i], x2[i], A12, A21)
        fa[i, 0] = yerror(e1inner_i, e2inner_i, x1[i], x2[i], y[i])
    return JaTrans.dot(fa)

def H(x):
    A12 = x[0, 0]
    A21 = x[1, 0]
    JaTrans = np.zeros((2, len(x1)))
    for i in range(0, len(x1)):
        JaTrans[0, i] = dfdA12(psat_wat, psat_dxn, x1[i], x2[i], A12, A21)
        JaTrans[1, i] = dfdA21(psat_wat, psat_dxn, x1[i], x2[i], A12, A21)
    return JaTrans.dot(JaTrans.transpose())


# Initialize Problem
prob = {'eps': 1e-3,
        'method': 'gradientDescent',
        'a': 1,
        't': 0.01,
        'b': 0.5,
        'itermax': 10000
        }

# Newton's Method
l = 0.01
a = np.array([[2],[1.5]])
e = 0.001;
for i in range(0, 10000):
    a = a + e*np.linalg.inv(H(a)+l*np.eye(2)).dot(g(a))

print(a)
