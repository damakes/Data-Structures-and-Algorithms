'''Sort characters
Write a program that takes a single string as its input and sort its characters from the lowest Unicode value to the highest Unicode value.
The program should print the new string.

The output from your program, when called with the code in the Test column, should be exactly as shown in the Result column:

Syöte         Tulos
wikipedia     adeiiikpw
assume        aemssu
'''

syote = input()
syote = ''.join(sorted(syote))
print(syote)



'''Arithmetic
Write a program that takes two integers, a and b, as input.
Your program should compute and display:
The sum of a and b
The difference when b is subtracted from a
The product of a and b
The quotient when a is divided by b
The remainder when a is divided by b
The result of log10 a
The result of
The output from your program, when called with the code in the Test column, should be exactly as shown in the Result column:

Syöte
  10
  2

Tulos
  10 + 2 is 12
  10 - 2 is 8
  10 * 2 is 20
  10 / 2 is 5.0
  10 % 2 is 0
  10 ^ 2 is 100
'''

def calculxte(x,y):
    print(f"{x} + {y} is {x + y}")
    print(f"{x} - {y} is {x - y}")
    print(f"{x} * {y} is {x * y}")
    print(f"{x} / {y} is {x / y}")
    print(f"{x} % {y} is {x % y}")
    print(f"{x} ^ {y} is {x ** y}")


a = int(input())
b = int(input())

calculxte(a,b)

'''Squares
Write a program that prints a dictionary where the keys are numbers between 1 and N, and the values are square of keys.

Input Specification

The first line of input contains N
Output Specification

Print the dictionary

The output from your program, when called with the code in the Test column, should be exactly as shown in the Result column:

Syöte	  Tulos
10      {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

'''

N = int(input())

mydict = {i: i**2 for i in range(1, N+1)}

print(mydict)



'''Sum of the First n Positive Integers
Write a program that takes a positive integer, n, as input and then displays the sum of all of the integers from 1 to n.
The sum of the first n positive integers can be computed using the formula: sum = n *(n+1)/2

The output from your program, when called with the code in the Test column, should be exactly as shown in the Result column

Syöte	  Tulos
10      The sum of the first 10 positive integers is 55
4       The sum of the first 4 positive integers is 10
'''


n = int(input())

sum = int(n * (n+1)/2)

print(f'The sum of the first {n} positive integers is {sum}')



'''Count vowels
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

For example, if s = 'hello', your program should print:

Number of vowels: 2

The output from your program, when called with the code in the Test column, should be exactly as shown in the Result column:

Syöte	        Tulos
Restaurant    Number of vowels: 4
Air           Number of vowels: 2
'''


syote = input()

syote = syote.lower()

valid_vowels = {'a', 'e', 'i', 'o', 'u'}

vowels = 0

for i in syote:
  if i in valid_vowels:
    vowels += 1

print(f'Number of vowels: {vowels}')



'''Sum a Collection of Numbers
Write a program that sums all of the numbers taken as input, while ignoring any input that is not a valid number.
Your program should display the current sum after each number is entered. It should display an error message after each non-numeric input, and then continue to sum any additional numbers entered by the user.  The program exits when the user enters 0.
Ensure that your program works correctly for both integers and floating-point numbers.
The output from your program, when called with the code in the Test column, should be exactly as shown in the Result column:

Syöte
  12
  6
  11
  0
  200
  hello
  10
  0

Tulos
  The total is now 12.0
  The total is now 18.0
  The total is now 29.0
  The grand total is 29.0
  The total is now 200.0
  That wasn’t a number.
  The total is now 210.0
  The grand total is 210.0
'''

sum = 0

while True:

    syote = input()

    if syote == '0':
        break

    try:
        number = float(syote)
        sum += number
        print(f"The total is now {sum}")

    except ValueError:
        print("That wasn’t a number.")
        continue

print(f"The grand total is {sum}")


'''Custom encoder
Write a function called "custom_encoder" that accepts a string text as parameter and for each char of the text it calculates its 0-based position in the following reference string:

reference_string = 'abcdefghijklmnopqrstuvwxyz'

The function should return a list that contains all the positions. If a char is not found in the reference_string, its position should be -1'''


def custom_encoder(text):
    text = text.lower()
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    positions = []
    for char in text:
        if char in reference_string:
            positions.append(reference_string.index(char))
        else:
            positions.append(-1)
    return positions

'''Write a class Person that has a member function hello()
The output from your program, when called with the code in the Test column, should be exactly as shown in the Result column:

Testi
  p = Person('Matti')
  p.hello()

Tulos
  Hello, my name is Matti
'''


class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        hello = f'Hello, my name is {self.name}'
        print(hello)


'''Restaurant
Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
The output from your program, when called with the code in the Test column, should be exactly as shown in the Result column:

Testi
  restaurant = Restaurant('Kotipizza', 'pizza')
  print(restaurant.name)
  print(restaurant.cuisine_type)
  restaurant.describe_restaurant()
  restaurant.open_restaurant()

Tulos
  Kotipizza
  pizza
  Kotipizza serves wonderful pizza.
  Kotipizza is open. Come on in!
'''

class Restaurant:
  def __init__(self, restaurant_name, cuisine_type):
    self.name = restaurant_name
    self.cuisine_type = cuisine_type

  def describe_restaurant(self):
    print(f'{self.name} serves wonderful {self.cuisine_type}.')
  def open_restaurant(self):
    print(f'{self.name} is open. Come on in!')


'''User
Make a class called `User`. Create the following attributes: first_name and last_name, email, and location. Make a method called describe_user() that prints a summary of the user's information. Make another method called greet_user() that prints a personalized greeting to the user.
The output from your program, when called with the code in the Test column, should be exactly as shown in the Result column:

Testi
  Matti= User('Matti', 'Paajanen', 'mpaajanen', 'm.paajanen@gmail.com', 'Helsinki')
  Matti.describe_user()

  Maila= User('Maila', 'Halonen', 'm_halonen', 'm.halonen@mtv.fi', 'Vaasa')
  Maila.greet_user()

Tulos
  Name: Matti Paajanen
  Username: mpaajanen
  Email: m.paajanen@gmail.com
  Location: Helsinki

  Welcome back m_halonen!
'''

class User:
  def __init__(self, first_name, last_name, username,email, location):
    self.name = f'{first_name} {last_name}'
    self.username = username
    self.email = email
    self.location = location

  def describe_user(self):
    print(f'Name: {self.name}\nUsername: {self.username}\nEmail: {self.email}\nLocation: {self.location}')

  def greet_user(self):
    print(f'Welcome back {self.username}!')

'''Write a function to combine two lists
Write a function named combine_lists that accepts two lists of integers as parameters.
Consider that the two lists are already sorted (The numbers are already in order from smallest to biggest number).
Your function should return a list that combines the two lists and at the same time is itself also sorted.
To be clear all elements of the input lists should be in the output list and len(input_list1)+len(input_list2) == len(output_list).
Notice that your function should return the list, not print it.
You can use whatever you want as the name of the parameters.
You don't need to use any special function or functionality to complete the task.
Specially don't use any kind of sorting function of lists or Python in general.
Just normal Python list actions are enough for this task.
Iterate over the lists adding one by one the the smallest of the remaining elements of the two lists.
When one of the lists have been exhausted, you can just add the remaining elements of the other list to the output list.

Testi
  print(combine_lists([1, 3, 5, 7, 9], [0, 2, 4, 6, 8]))

Tulos
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

def combine_lists(output_list1, output_list2):
    output_list =  []

    for item in sorted(output_list2 + output_list1):
        output_list.append(item)

    assert len(output_list1) + len(output_list2) == len(output_list)

    return output_list
