def cached(function):
    cache = {}

    def decorated(*args, **nargs):
        nonlocal cache
        if cache.get(args):
            return cache[args]
        else:
            r = function(*args, **nargs)
            cache[args] = r
            return r

    return decorated


@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(20))
