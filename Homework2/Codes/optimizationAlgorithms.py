import numpy as np

# Get the step direction based on method
def getStep(x, prob, gradfun, Hessfun):
    if prob['method'] == 'gradientDescent':
        s = -gradfun(x)
    elif prob['method'] == 'newtonsMethod':
        s = -np.linalg.inv(Hessfun(x)).dot(gradfun(x))
    return s


def appendNewX(xarray, xnew):
    # Append new x vector to array of x at each iteration
    return np.concatenate((xarray, xnew))

def appendNewF(farray, fnew):
    # Add new value of f to solution array
    return np.append(farray, fnew)

def lineSearch(x0, prob, xiter, fiter, fun, gradfun, Hessfun = []):
    # x     - the initial x guess
    # prob  - the problem dict with settings.  The prob dict has the
    #         following structure:

        # prob = {
        #         'eps': 1e-6,                    ----- value is the convergence tolerance
        #         'method': 'gradientDescent',    ----- 'gradientDescent' or 'newtonsMethod'
        #         'a': 1,
        #         't': 0.01,
        #         'b': 0.5,
        #         'itermax': 10000,               ----- max iterations before stopping
        #         }

    # xiter - array of x values at iteration step, this array will grow with every iteration.
    #         Enter a row of initial x values here.
    # fiter - array of f values at iteration step, this array will grow with every iteration.
    #         Enter a row of initial f values here.
    # gradfun - gradient function
    # Hessfun - Hessian function (optional)
    iter = 0
    x = x0
    defaultAlpha = prob['a']
    while True:
        # If norm of gradient is greater than predefined
        # value, then break out of while loop.  Solution has converged.
        G = gradfun(x)
        if np.linalg.norm(G, ord=2) < prob['eps']:
            break
        # If iteration count reaches maximum allowable iterations, then break
        if iter >= prob['itermax']:
            print("Solution did not converge in {} iterations using {}".format(
                    prob['itermax'],
                    prob['method']))
            break

        # Iterate
        s = getStep(x, prob, gradfun, Hessfun)
        fAlpha = fun(x + prob['a']*s)
        phi = fiter[len(fiter)-1] + prob['a']*prob['t']*G.transpose().dot(s)
        while fAlpha > phi: # backtrack step if necessary
            prob['a'] = prob['b']*prob['a']
            fAlpha = fun(x + prob['a']*s)
            phi = fiter[len(fiter)-1] + prob['a']*prob['t']*G.transpose().dot(s)
        # Set new position
        x = x + prob['a']*s

        # Save Necessary Iteration Data
        xiter = appendNewX(xiter, np.array([x]))
        fiter = appendNewF(fiter, fAlpha)
        prob['a'] = defaultAlpha
        iter += 1

    return [iter, xiter, fiter]
