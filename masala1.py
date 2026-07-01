# 1-masala

def fib_(n):
    a = 0
    b = 1
    new = []
    for i in range(n+1):
        new.append(a)
        a, b = b, a + b
    return new
print(fib_(4))





