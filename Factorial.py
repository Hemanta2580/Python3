"program for factoeial with out recurrsion"
fact=1
print("enter the number ")
n=int(input("the number is "))
if n==0:
    print(f"the factorial of {n} is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print(f"the factorial of {n} is ",fact)

# factorial with recurrsion

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        fact=n*factorial(n-1)
        return fact
print("enter the number ")
c=int(input("the number is = "))
fact1=factorial(c)
print(f"the factorial number of {c} is",fact1)
