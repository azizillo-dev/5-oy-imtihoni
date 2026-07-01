
text = input("Textni kiriting: ")

def generator(text):
    sozlar = text.split()
    for i in sozlar:
        yield i
gen = generator(text)

print(next(gen))
print(next(gen))
print(next(gen))

