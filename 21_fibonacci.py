# Fibonacci
# 1 1 2 3 5 8 13 21...

def fib_cache(function):
    cache = {}

    def decorator(args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = function(args)
            return cache[args]

    return decorator


@fib_cache
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-2) + fib(n-1)

print(fib(50))
"""
fib(8) -> 
  fib(6) + fib(7) ->
    fib(4) + fib(5) + fib(5) + fib(6) ->
      fib(2) + fib(3) + fib(3) + fib(4) + fib(3) + fib(4) + fib(4) + fib(5) ...
      ...
"""
