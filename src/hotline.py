import math
import time

def binomial_coefficient(n, k):
    return math.comb(n, k)

def get_coef(n, k):
    if k == 0:
        return 1
    return (n * get_coef(n - 1, k - 1) // k)

def factorial(nbr):
    if nbr == 0:
        return 1
    return math.prod(range(1, nbr + 1))

def binomial_distribution(calls, prob):
    overload = 0
    for k in range(51):
        if k != 0 and k % 5 == 0:
            print()
        elif k != 0:
            print("\t", end="")
        res = get_coef(calls, k) * (prob ** k) * ((1 - prob) ** (calls - k))
        print(f"{k} -> {res:.3f}", end="")
        if k <= 25:
            overload += res
    return overload

def poisson_distribution(exp):
    overload = 0
    for k in range(51):
        if k != 0 and k % 5 == 0:
            print()
        elif k != 0:
            print("\t", end="")
        res = (math.exp(-exp) * (exp ** k)) / factorial(k)
        print(f"{k} -> {res:.3f}", end="")
        if k <= 25:
            overload += res
    return overload

def hotline(arg1, arg2=None):
    hours = 8
    calls = 3500
    prob = arg1 / (hours * 60 * 60)
    exp = calls * prob

    if arg2 is not None:
        n, k = arg1, arg2
        result = binomial_coefficient(n, k)
        print(f"{k}-combinations of a set of size {n}:")
        print(result)
    else:
        print("Binomial distribution:")
        overload_binomial = binomial_distribution(calls, prob)
        print("\nOverload: {:.1f}%".format((1 - overload_binomial) * 100))
        print("Computation time: {:.2f} ms".format(time.process_time() * 1000))

        print("\nPoisson distribution:")
        overload_poisson = poisson_distribution(exp)
        print("\nOverload: {:.1f}%".format((1 - overload_poisson) * 100))
        print("Computation time: {:.2f} ms".format(time.process_time() * 1000))
