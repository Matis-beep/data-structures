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

def power(x,y):
    print("calling power(",x,"),",y,")")

    if y ==1:
        print("base cape reached:power(",x",1)=",x)
        return x
    else:
        half=power(x,y//2)
    
    if y % 2==0:
        result =half * half
        print("returning", result,"for power (",x,",",y,")")
        return result
    else:
        result=x * half * half
        print("returning", result,"for power (",x,",",y,")")
        return result
print("Final answer:",power(3,5))