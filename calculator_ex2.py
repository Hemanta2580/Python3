def subtraction1(a,b):
    return (a-b)
def add1(a,b):
    return(a+b)
def multiplication1(a,b):
    return(a*b)
def divition1(a,b):
    return  (a/b)
def reminder1(a,b):
    return(a%b)

if __name__=='__main__':
    while 1:
        print("welcome to the calculator")
        print("press 1 for \"addition\"\npress 2 for \"subtraction\"\npress 3 for \"multiplication\"\npress 4 for \"divition\"\npress 5 for \"reminder\"")
        print("press other number to quit")
        c=int(input())
        if c==1:
            print("enter the number you want to add")
            x=int(input())
            y=int(input())
            r=add1(x,y)
            print(f"the addition of {x},{y} is {r} ")
            continue

        elif c==2:
            print("enter the number you want to subtract")
            x = int(input())
            y = int(input())
            r = subtraction1(x, y)
            print(f"the subtraction of {x},{y} is {r} ")
            continue
        elif c==3:
            print("enter the number you want to add")
            x = int(input())
            y = int(input())
            r = multiplication1(x, y)
            print(f"the multiplication of {x},{y} is {r} ")
            continue
        elif c==4:
            print("enter the number you want to add")
            x = int(input())
            y = int(input())
            r = divition1(x, y)
            print(f"the divition of {x},{y} is {r} ")
            continue
        elif c==5:
            print("enter the number you want to add")
            x = int(input())
            y = int(input())
            r = reminder1(x, y)
            print(f"the reminder of {x},{y} is {r} ")
            continue
        if x=='q':
            quit();
        else:
            quit()







