# def hello(name="Guest"):
#     print(f"Hello {name}!")

# hello("Raj")
# person="Garry"
# hello(person)

# def adder(x=10, y=20):
#     return x+y
# print(adder())

# x = 100 #global
# def test():
#     print(x)
# test()

# x = 100
# def test(y):
#     global x
#     print(f"global: {x} \nlocal: {y}")
# test(10)

# n = 23
# def tester(n):
#     n = 21
#     print(n)
# tester(19)

def hello(name):
    print(f"Hello {name}")
def cityName(city, name):
    hello(name)
    print(f"Welcome to {city}")

cityName("Mumbai", "Laraib")