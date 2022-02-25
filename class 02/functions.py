#def word means to define/call/initialise a function.
#declaring a fucntion
def greet():
    print('hello')

#calling the function
greet()

def greet_by_name(name):
    print(f'Hello {name}')

greet_by_name('Jay')

def get_factorial(number):
    output = number
    for i in range(1, number):
        output *= i # output = output*i(the code written is just a sorted version :P)
    return output

a=get_factorial(5)
print(a)

#optional parameter function
def greet_by_name(name='joke'):#here if you dont input any value of name while calling the function, the default value will be 'Joke'
    print(f'Hello {name}')

greet_by_name('Jay')