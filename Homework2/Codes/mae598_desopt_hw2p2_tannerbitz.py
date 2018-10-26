#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, rc

from optimizationAlgorithms import *

#   Define the objective function f(x),
#   it's gradient g(x), and it's Hessian H(x)

#   Note: In homework problem x[0] == x2 and x[1] == x3

def getx1(x):
    # Get x1 value based on x2 and x3
    # x2 = x[0]
    # x3 = x[1]
    return 1 - 2*x[0] - 3*x[1]


def f(x):
    return (2-2*x[0]-3*x[1])**2 + x[0]**2 + (x[1]-1)**2

def g(x):
    return np.array([-8, -14]) + np.array([[10, 12],[12, 20]]).dot(x)

def H(x):
    return np.array([[10, 12],[12, 20]]);


############################################################
#                Set up Problem and Run                    #
############################################################

x0 = np.array([-1, -1]) # Initial Point

################## Gradient Descent ########################
xiter_g = np.array([[x0[0], x0[1]]]) # value of x at each iteration
fiter_g = np.array([f(x0)]) # value of function at each iteration

prob = {
        'eps': 1e-6,
        'method': 'gradientDescent',
        'a': 1,
        't': 0.01,
        'b': 0.5,
        'itermax': 10000,
        }

[iterationsToFinish_g, xiter_g, fiter_g] = lineSearch(x0, prob, xiter_g, fiter_g, f, g)


print("The global minimum occurs at the point \n{}".format(xiter_g[len(xiter_g)-1]))
print("The minimum value of the objective function is {}".format(fiter_g[len(fiter_g)-1]))
print("The solution was found in {} iterations\n".format(iterationsToFinish_g))




###########              Newton's Method                   #############
xiter_n = np.array([[x0[0], x0[1]]]) # value of x at each iteration
fiter_n = np.array([f(x0)]) # value of function at each iteration

prob = {
        'eps': 1e-6,
        'method': 'newtonsMethod',
        'a': 1,
        't': 0.01,
        'b': 0.5,
        'itermax': 10000,
        }

[iterationsToFinish_n, xiter_n, fiter_n] = lineSearch(x0, prob, xiter_n, fiter_n, f, g, H)

print("The global minimum occurs at the point \n{}".format(xiter_n[len(xiter_n)-1]))
print("The minimum value of the objective function is {}".format(fiter_n[len(fiter_n)-1]))
print("The solution was found in {} iterations.".format(iterationsToFinish_n))



# Contour Plot of Objective Function Minimization
fig = plt.figure()
ax = fig.add_subplot(111)
x = np.linspace(-1.5, 2.0, 100)
y = np.linspace(-1.5, 2.0, 100)
X, Y = np.meshgrid(x, y)
F = np.zeros(X.shape)
[ix, jx] = X.shape
for i in range(0, ix):
    for j in range(0, jx):
        F[i,j] = f(np.array([X[i,j], Y[i,j]]))

surf = ax.contourf(X, Y, F, cmap=cm.coolwarm)
plotgraddescentpath = ax.plot(xiter_g[:, 0], xiter_g[:, 1], color='yellow', label='Gradient Descent')
plotnewtonsmethodpath = ax.plot(xiter_n[:,0], xiter_n[:, 1], color='orange', label='Newtons Method')
plt.xlabel('x2')
plt.ylabel('x3')
plt.title('Objective Function as a function of x2 and x3')
ax.legend()

plt.show()


# Log linear convergence plot
fdist = fiter_g - fiter_g[len(fiter_g)-1]
x = np.arange(1, len(fdist)+1)
fdist_n = fiter_n - fiter_n[len(fiter_n)-1]
x_n = np.arange(1, len(fdist_n)+1)

fig2 = plt.figure()
plt.rc('text', usetex=True)
plt.semilogy(x, fdist, label='Gradient Descent')
plt.semilogy(x_n, fdist_n, label='Newtons Method')
plt.xlabel('Iterations (k)')
plt.ylabel(r'$\log (f_k-f^*)$')
plt.legend()
plt.title('Convergence Log-Linear Plot')
plt.show()
