a = [2, 4, 5, 6, 8, 9, 33, 45, 22]

# def func(lst):
#     b = []
#     c = 0
#     for i in lst:
#         c += i
#         b.append(c)
#     return b
# print(func(a))



# 2-masala
def decorator(func):
    def wrapper(a):
        b = []
        c = 0
        for i in a:
            c += i
            b.append(c)
        return func(b)
    return wrapper

@decorator
def yangi(a):
    return a
print(yangi(a))














