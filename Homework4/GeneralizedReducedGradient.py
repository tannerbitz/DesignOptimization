import numpy as np

def dzdd(sk, dk, dfdd, dfds, dhds, dhdd):
    # This function calculates and returns the partial derivates of the reduced
    # gradient fucntion w.r.t. the decision variables at the current iteration

    ########## INPUTS ###############
    # sk - state variables at iteration k
    # dk - decision variables at iteration k
    # dfdd - function to calculate dfdd (with dk as input)
    # dfds - funciton to calculate dfds (with sk as input)
    # dhds - function to calculate dhds (with sk as input)
    # dhdd - function to calculate dhdd (with dk as input)
    dfdd_k = dfdd(dk)
    dfds_k = dfds(sk)
    dhds_k = dhds(sk)
    dhdd_k = dhdd(dk)
    return dfdd_k + dfds_k.dot(np.linalg.inv(dhds_k)).dot(dhdd_k)


def dk1(sk, dk, alphak, dfdd, dfds, dhds, dhdd):
    # This function iterates the decision variables and returns d_k+1

    ########## INPUTS ###############
    # sk - state variables at iteration k
    # dk - decision variables at iteration k
    # alphak - step size coefficient
    # dfdd - function to calculate dfdd (with dk as input)
    # dfds - funciton to calculate dfds (with sk as input)
    # dhds - function to calculate dhds (with sk as input)
    # dhdd - function to calculate dhdd (with dk as input)
    global dzdd
    dzdd_k = dzdd(sk, dk, dfdd, dfds, dhds, dhdd)
    return dk - alphak*dzdd_k.transpose()

def skp1(sk, dk, alphak, dfdd, dfds, dhds, dhdd):
    # This function calculates s_prime_k+1

    ########## INPUTS ###############
    # sk - state variables at iteration k
    # dk - decision variables at iteration k
    # alphak - step size coefficient
    # dfdd - function to calculate dfdd (with dk as input)
    # dfds - funciton to calculate dfds (with sk as input)
    # dhds - function to calculate dhds (with sk as input)
    # dhdd - function to calculate dhdd (with dk as input)
    global dzdd
    dhds_k = dhds(sk)
    dhdd_k = dhdd(dk)
    dzdd_k = dzdd(sk, dk, dfdd, dfds, dhds, dhdd)
    return sk + alphak*np.linalg.inv(dhds_k).dot(dhdd_k).dot(dzdd_k.transpose())

def iteratesk(sk, dk, dhds, h):
    # This function iterates sk during the convergence step of sk+1, after dk+1 has been calculated

    ########## INPUTS ###############
    # sk - state variables at iteration k
    # dk - decision variables at iteration k
    # dhds - function to calculate dhds (with sk as input)
    # h - function to calculate the constraint values at the current iteration
    dhds_k = dhds(sk)
    hsd = h(dk, sk)
    return sk - np.linalg.inv(dhds_k).dot(hsd)

def sk1(sk, dk, alphak, dfdd, dfds, dhds, dhdd, h, epsilon):
    # This function iterates the state variables and returns s_k+1

    ########## INPUTS ###############
    # sk - state variables at iteration k
    # dk - decision variables at iteration k
    # alphak - step size coefficient
    # dfdd - function to calculate dfdd (with dk as input)
    # dfds - funciton to calculate dfds (with sk as input)
    # dhds - function to calculate dhds (with sk as input)
    # dhdd - function to calculate dhdd (with dk as input)
    # h - function to calculate the constraint values at the current iteration
    # epsilon - limit of convergence criteria
    global dzdd
    sk = skp1(sk, dk, alphak, dfdd, dfds, dhds, dhdd)
    h_k = h(dk, sk)
    while (np.linalg.norm(h_k) > epsilon):
        sk = iteratesk(sk, dk, dhds, h)
        h_k = h(dk, sk)
    return sk


def GRG(d0, s0, epsilon, alphak, dfdd, dfds, dhds, dhdd, h):
    # This function calculates the generalized reduced gradient

    ########## INPUTS ###############
    # s0 - initial state variables
    # d0 - initial decision variables
    # epsilon - limit of convergence criteria
    # alphak - step size coefficient
    # dfdd - function to calculate dfdd (with dk as input)
    # dfds - funciton to calculate dfds (with sk as input)
    # dhds - function to calculate dhds (with sk as input)
    # dhdd - function to calculate dhdd (with dk as input)
    # h - function to calculate the constraint values at the current iteration
    global dzdd
    dk = d0
    sk = s0
    dzdd_k = dzdd(sk, dk, dfdd, dfds, dhds, dhdd)
    cnt = 0
    itermax = 10000
    while (np.linalg.norm(dzdd_k) > epsilon or cnt == itermax):
        dk = dk1(sk, dk, alphak, dfdd, dfds, dhds, dhdd)
        sk = sk1(sk, dk, alphak, dfdd, dfds, dhds, dhdd, h, epsilon)
        dzdd_k = dzdd(sk, dk, dfdd, dfds, dhds, dhdd)
        cnt += 1
    if (cnt == itermax):
        print("A solution wasn't reached in {} iterations".format(cnt))
    else:
        print("A solution was reached in {} iterations".format(cnt))
        print("d: {}".format(dk))
        print("s: {}".format(sk))
