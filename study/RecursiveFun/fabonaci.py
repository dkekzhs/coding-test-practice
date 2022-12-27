def fabo(n):
  if n <= 1:
    return n;
  return fabo(n-1) + fabo(n-2);

# print(fabo(30))


# Fibonacci (반복): O(n)
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fib(30))