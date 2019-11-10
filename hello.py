''' Dictionaries '''
person = {
    "name" : "Charith",
    "age": 37,
    "occupation": "Software Engineer"
}

person["location"] = "Sri Lanka"
print(person)

# print(person["name"])
# print(person.get("Name"))
# print(person.get("status", "single")) # Second arg specifies a default value


''' Unpacking '''
# names = ('Sara', 'Melissa', 'John', 'Mark')
# i, j, k, l = names;
# print(i, j, k, l)


''' Tuples '''
# immutable
# names = ('Sara', 'Jenny', 'Lola')


''' Remove duplicates '''
#names = ['Mona', 'Mimi', 'Marko','Mimi', 'Melissa', 'Marko','Mimi']

# SOLUTION 2
# uniques = []
# for name in names:
#     if name not in uniques:
#         uniques.append(name)
# print(uniques)

# SOLUTION 1
# for name in names:
#     while names.count(name) > 1:
#         names.remove(name)
# print(names)

''' List operations '''
# numbers = [1, 5, 3, 4, 2, 2, 7]
# numbers.append(10)
# numbers.insert(1, 6);
# numbers.remove(3) # removes number 3 not index 3
# #numbers.clear() # clears the list
# del numbers[0] # deletes a specific index
# a = numbers[:2] + numbers[3:]
# #b = numbers.copy() # copies a list
# print(numbers.count(2)) # counts the occurances of 2
# print(a)
# print(numbers)

''' Largest number in a list '''
# numbers = [1, 5, 10 , 2 , 20, 8, 4]
# currentLargest = 0
# for i in numbers:
#     if currentLargest < i:
#         currentLargest=i

# print(currentLargest)

''' Nested loops '''
# loopInstructions = [ 5, 2, 5, 2, 2]

# for i in loopInstructions:
#     print("*" * i)

# for i in range(10):
#     for j in range(10):
#         print(f'({i},{j})')

''' For in '''
# RANGE(start, end, stepping)
# for i in range(0,50, 5):
#     print("*" * i)

# for element in ['Apples','Oranges','Cabbages','Drumsticks']:
#     print(element)

''' Loops '''
# loopUntil = 0;
# while loopUntil < 50:
#     print("*" * loopUntil * 2)
#     loopUntil += 1

''' Conditional operators '''
# isRich = False
# isDumb = True

# if isRich and isDumb:
#     print("You'll be a great politician")
# elif isRich and not isDumb:
#     print("You'll make a great businessman")
# elif not isRich and isDumb:
#     print("Well you're fucked")
# else:
#     print("You'll be a great person!")


''' Conditions '''
# isCold = True;
# isHot = False;

# if isCold:
#     print("Its cold!")
# elif isHot:
#     print("Its hot")
# else:
#     print("Have a nice day!")


''' Operators '''
# print(10/3)
# print(10//3)
# print(10%3)
# print(10**3)


''' Finding text '''
# src = input("Enter text: ")
# search = input("Enter search text: ")
# pos = src.find(search)
# isfound = search in src

# print("Is text found: " +str(isfound))
# print("Search text found at: " + str(pos))


''' Weight calculator '''
# message = input("\nEnter your name: ");
# weight = input("\nEnter your weight in lbs: ");
# weight_kg = float(weight) * 0.45;

# print(f'''
#     Your weight in Kgs: {weight_kg}
# ''')
