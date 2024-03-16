# Functions
a = "Hello World"
print(a)

# Replace()
a.replace("World", "Universe")
print(a)

# Defining your own function, def: Return

#def functionname(parameter): Expression, code of what function should return answer

# eg. determine if a number is a prime number, using % modulus operator and for loop and if
def checkIfPrime(numberToCheck):
    for x in range(2, numberToCheck):
        if(numberToCheck%x == 0):
            return False
        return True
Answer = checkIfPrime(13)
print(Answer)
print()


# Variable scope concept when defining a function
'''variable defined/declared inside a function (local)
are treated differently from variables defined
outside a function (global)'''
'''local variable accessible only inside a function,
global variable is accessible anywhere in the program'''

message1 = "Global Variable"

def myfunction():
    print("\nINSIDE THE FUNCTION") # Global Variable are accessible inside a function
    print(message1)
    
    # Declaring a local variable message2 = "Local Variable"
    print(message2)
message2 = "Local Variable"

# Calling the function myfunction()
print("\nOUTSIDE THE FUNCTION")
# Global variables are accessible outside the function
print(message1)
# Local variable are NOT accessible outside function
print(message2)
    
print()

# If global and local variables share similar names
'''any code inside the function is accessing the local variable
and any code outside is accessing the global variable'''

message1 = "Global Variable (share same name as a loal varible)"

def myfunction2():
    message1 = "Local Variable (shares same name as a global variable)"
    print("\nINSIDE THE FUNCTION")
    print(message1)
# Calling the function myFunction2()
# Printing message1 OUTSIDE the function print("\nOUTSIDE THE FUNCTION")
    print(message1)
    
print()
