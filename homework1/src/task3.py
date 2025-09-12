'''
 Create an if statement to check if a given number is positive,
negative, or zero. Implement a for loop to print the first 10 prime numbers (you may need to
research how to calculate prime numbers). Create a while loop to find the sum of all numbers from
1 to 100.
'''

# Function to check to see if a number is positive or negative. 
def isPos(num):
    if num > 0:
        return True

# Function that will print the first 10 prime numbers
def primeNumbers():

    # Number of prime numbers to print
    numOfPrimes = 0
    primeList = []

    # Outer for loop to loop through numbers from 2 to 100
    for n in range(2,100):

        # boolean to keep track of prime numbers
        isPrime = True

        # Inner for loop to check to see if a number (n) is divisible by any other number
        for i in range(2,n):

            #If n is divisible by another number isPrime is set to False
            if n % i == 0:
                isPrime = False
                break
        
        # if isPrime is true then we have a prime number and we can print it out as long as we have less than 10 numbers printed
        if numOfPrimes < 10 and isPrime:
            primeList.append(n)
            print(n)
            numOfPrimes += 1
            
    return primeList

# Funtion that will find the sum of all of the numbers from 1 to 100
def sumOfNums():

    sum = 0
    count = 0

    while count < 101:
        sum += count
        count += 1

    print(sum)

    return sum