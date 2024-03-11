#function defined to checks if number is prime
def checkIfPrime (numberToCheck):
    for x in range(2, numberToCheck):
        if (numberToCheck%x == 0 ):
            return False
        return True
# call the function
checkIfPrime(13)
# assign a variable to the function
#answer = checkIfPrime(13)
#print(answer)
