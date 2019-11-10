''' Exceptions '''
try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError:
    print("Invalid input!")

''' Functions '''

# def square(number):
#     return number * number

# print(square(10))

# def setName(first, last):
#     print(f'{first} {last}')

# # Positional args - order matters
# setName("Charith","Rathnayake")
# # Keyword args
# setName(last="Rathnayake", first="Charith")

# def hello(name):
#     print(f'Hello {name}!')

# hello("Charith")