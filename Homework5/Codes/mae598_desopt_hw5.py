#!/usr/bin/python3
import numpy as np


x0 = np.array([[1],[1]]);
mu0 = np.array([[0],[0]])
W = np.eye(2)


active = [ 1]


def cons(active_vec, x_vec):
    # x_vec: nparray ------- x1 = x_vec[0], x2 = x_vec[1]
    c1 = lambda x: x[1]**2 - 2*x[0]
    c2 = lambda x: (x[1] - 1)**2 + 5*x[0] - 15
    C = [c1, c2]

    res = np.array([])
    for i in range(0, len(active_vec)):
        res = np.append(res, C[active_vec[i]](x_vec))
    res = np.resize(res, (res.shape[0], 1))
    return res

def dcons(active_vec, x_vec):
    dc1dx = lambda x: np.array([[-2, 2*x[1]]])
    dc2dx = lambda x: np.array([[5, 2*(x[1] -1)]])

    dCdx = [dc1dx, dc2dx]

    res = np.array([])
    for i in range(0, len(active_vec)):
        res = np.append(res, dCdx[active_vec[i]](x_vec))
    res = np.resize(res, (len(active_vec), 2))
    return res


def solve_qp(W, A, c, b)
    # This function solves the QP
    #
    #       min    1/2 s.T * W * s + c.T *s
    #        s
    #       s.t.   A * s - b = 0
    #
    # The algorithm to solve this QP is based on Dr. Ren's "Algorithms for Constrained Optimization, slide 24"

    if (A.size == 0):
        mat = W
    else:
        mat_top = np.concatenate((W, A.T), axis=1)
        mat_bot = np.concatenate((A, np.zeros((A.shape[0], A.shape[0]))), axis=1)
        mat = np.concatenate((mat_top, mat_bot), axis=0)

    if (b.size == 0):
        vec = -c
    else:
        vec = np.concatenate((-c, b), axis=0)
    return np.linalg.inv(mat).dot(vec)


W = np.array([[1, 2], [3, 4]])
A = np.array([[2, 1]])
c = np.array([[2],[4]])
b = np.array([[1]])

print(solve_qp(W, A, c, b))

def line_search(fk, obj_fun):
    alpha = 1
    phi  = lambda fk, alpha, t, sk: fk + alpha*t*sk

    phi_k
