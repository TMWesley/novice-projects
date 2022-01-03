Width = 19
Length = 12
print(Length * Width)

prefix = 'Py'
print(prefix + 'thon')

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

x = float(input('Please enter your age:'))
if x > 120:
    print('Sorry, this is not a valid number, please try again')

list(range(0, 10))

input('how are you today?')

def greet(*user_name):
    """This function gives a good morning greeting to the person passed into the function"""
    for name in user_name:
        print('Hello, ' + name)


greet("Tiffany", "Charlie", "Robert", "Samantha")

print(greet.__doc__)

def absolute_value(num):
    """ This function returns the absolute value of the given number"""
    if num >= 0:
        return num
    else:
        return -num
print(absolute_value(-18))

def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ', ' + msg)


greet("Kate")
greet("How do you do?", "Bruce")

def greetings(name, msg='Good morning!'):
    """function says good morning by default"""
    print('Hello,' + name + msg, end=',')
    print(msg)

greetings('Tiffany', msg='Good night!')

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Would you like to turn off your computer?')

colby = str('Hello to my baby blue')

print(colby)

newtry = list(('apple', 'cherry', 'banana'))

print(newtry)

fruits = ['apple', 'cherry', 'banana']
del fruits[0]
fruits.append('pina colada')
print(fruits)

from collections import deque
names = deque(['Eric', 'John', 'Michael'])
names.append('Terry')
names.append('Graham')
names.popleft()
names.popleft()
print(names)

#going to try to write my own rock, paper scissors script
#first, I need to write the computers moves

input('Choose your weapon')

tel = {'jack': 4098, 'sape': 4139}
'guido' in tel
print(list(tel))

veejay = 1
while veejay < 5:
    veejay = veejay + 1
    print(veejay)


word = 'asparagus'
turns = 12
while turns > 0:
    guess = ''
    for letter in word:
        if letter in guess:
            print(letter)

        else:
            guesses = input(print('what is your guess?'))
            print ('_')
            turns -= 1
            guesses += guesses
