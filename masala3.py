from collections import namedtuple


Car = namedtuple("Car", ['brand', 'model', 'year', 'mileage'])

cars = [
    Car("BMW", "M5F90", 2025, 10000),
    Car("Mercedes", "G63", 2026, 10300),
    Car("Lambarghini", "S3", 2026, 10200),
    Car("GM", "Nexia 3", 2026, 10700),
    Car("BVD", "Song Plus", 2026, 12000)
]

eng_kam_yurgan = min(cars, key = lambda x: len(str(x.mileage)))
print(f"""----Eng kam yurgan mashina----
      Modeli: {eng_kam_yurgan.model}
      Brandi: {eng_kam_yurgan.brand}   
      Yili: {eng_kam_yurgan.year}   
      Yurgani: {eng_kam_yurgan.mileage}   
""")







