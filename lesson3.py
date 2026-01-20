def fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

for i in range(7):
    print(fibonacci(i))

def factorial(n):
    if n==1:
        print("reached base case")
        return 1
    else:
        print("calling factorial(",n-1,")")
        return n*factorial(n-1)
    print(factorial(5))

def sumOfNumber(n):
    print(" Calling sumOfNumber( ",n,")")

    if n==0 or n==1:
        print("base cap reached with the n =",n)
        return n
    else:
        result = n + sumOfNumber(n-1)
        print("returning",result,"for n=",n)
        return result
    
print("Final answer:",sumOfNumber(5))