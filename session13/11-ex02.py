import time


def fib(n):
    """
    an intuitive version of fibonacci
    """
    global number_fib_calls
    number_fib_calls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)


known = {1: 1, 2: 2}


def fib_efficient(n):
    """
    a "memori version of fibonacci
    """
    global number_fib_calls
    number_fib_calls += 1
    if n in known:
        return known[n]
    else:
        ans = fib_efficient(n - 1) + fib_efficient(n - 2)
        known[n] = ans
        return ans


number_fib_calls = 0
fib_args = 32

time_begin = time.time()
print(fib(fib_args))
time_end = time.time()
print('function calls', number_fib_calls)
print('function run time', time_end - time_begin)

number_fib_calls = 0

time_begin = time.time()
print(fib_efficient(fib_args))
time_end = time.time()
print('function calls', number_fib_calls)
print('function run time', time_end - time_begin)
