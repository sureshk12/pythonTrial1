import sys

print(sys.version)
print(sys.executable)

def greet(who_to_greet):
    """Function printing python version."""
    greeting = "Hello, {}".format(who_to_greet)    
    return greeting

print(greet('World'))
print(greet('Suresh'))

