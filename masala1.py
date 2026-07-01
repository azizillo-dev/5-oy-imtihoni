# 1-masala

def fib_(n):
    a = 0
    b = 1
    new = []
    for i in range(n):
        new.append(a)
        new.append(b)
        a, b = b, a + b
    return new
print(fib_(4))





