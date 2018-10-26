#!/usr/bin/python3
import numpy as np
from GeneralizedReducedGradient import GRG

#  THESE WOULD BE CHANGED FOR A DIFFERENT PROBLEM

def dfdd(d):
    # Function to calculate the partial derivative of the objective function w.r.t.
    # the decision variables, d
    # d - np array with shape (n-m, 1)
    return 2*d

def dfds(s):
    # Function to calculate the partial derivates of the objective function w.r.t.
    # the state variables, s
    # s - np array with shape (m, 1)
    return np.array([[2*s[0, 0], 2*s[1, 0]]])

def dhds(s):
    # Function to calculate the partial derivates of the constraints w.r.t.
    # the state variables, s
    # s - np array with shape (m, 1)
    return np.array([[2/5*s[0, 0], 2/25*s[1, 0]], [1, -1]])

def dhdd(d):
    # Function to calculate the partial derivates of the constraints w.r.t.
    # the decision variables, d
    # d - np array with shape (n-m, 1)
    return np.array([[d[0, 0]/2],[1]])

def constraints(d, s):
    # Function to calculate the value of the constraints at each iteration k
    # d - np array with shape (n-m, 1)
    return np.array([[1/4*d[0, 0]**2 + 1/5*s[0, 0]**2 + 1/25*s[1, 0]**2 - 1],
                     [d[0, 0] + s[0, 0] - s[1, 0]]])


def main():
    d0 = np.array([[1]])
    s0 = np.array([[1], [1]])
    epsilon = 1e-6 # this is used in the convergence critera
    alphak = 1e-2  # coefficient of step size
    GRG(d0, s0, epsilon, alphak, dfdd, dfds, dhds, dhdd, constraints)

main()
