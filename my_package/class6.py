#set... 

a={3,34,56, 3, 3 , "bggs"}
print(type(a))
print(a)
a.add("india")
print(a)

b= a.copy()
print(b)
b.clear()
print(b)


#elemnt remove kora..
b.discard(3)
print(b)
## pop method randomly  jkono elemnt remove kore..
b.pop()
print(b)
b.remove("bggs")
print(b)


#duita set ke combine kora..
x=[2,34,"ami"]
b.update(x)
print(b)


#union ..intersection..

a={34, 45, 56 ,67, "bangladesh", 45}
b= {2,3, "bangladesh",45}

print(a.intersection(b))
print(a.difference(b))
#union ar update mutamuti same...
print(a.union(b))



###function...

def myfunc():
    print("Hello world")

myfunc()

def  add(a,b):
     print(a+b)

add(2,3)


# ##..assigning argument value..
def add(a, b=0):
    print(a-b)

add(4)    


def add(a, b=0):
    print(a-b)
    print(a+b)
    print(a*b)
    print(a/b)
    print(a%b)

add(4,8)    


while True:
    x=int(input("Enter a number"))
    y = int(input("enter second number"))


    def add2(a,b=0):
        print(a-b)
        print(a+b)
        print(a*b)
        print(a/b)
        print(a%b)

    add2(x, y) 

    is_continue=input("Type yes for continue or no for exit  ").lower()

    if(is_continue=="yes"):
        pass
    else:
        break

   ## using return...   ut aktai retun korte pre..
while True:
    x=int(input("Enter a number"))
    y = int(input("enter second number"))


    def add2(a,b=0):
        return(a-b)
       

    y= add2(x, y) 
    print(y+50)

    is_continue=input("Type yes for continue or no for Exit  ").lower()

    if(is_continue=="yes"):
        pass
    else:
        break


## user randomly onk gulo parameter dile..
def foo(*a):
    sum=0
    for i in a:
        sum+=i       
    return sum


y=foo(1,1,1,1,1)
print(y+10)   

##user er kach theke input niye...namta banano.. 
# while True:
#     num= int(input("enter a number : "))
#     for i in range(1,11):
#         print(f'{num} X {i}={num*i}')


# prevoius ta kno exit point nei...
# eta diye exit point banabo..

# while True:
#     num= int(input("enter a number : "))
#     if(num==0):
#         break
#     else:
#         for i in range(1,11):
#             print(f'{num} X {i} = {num*i}')


def solve(*a):
    sum=0
    for i in a:
        sum+=i
    return sum
    
x=[]   
while True:
    num = int(input("Enter a number : "))
    if(num==0):
        break
    else:
        x.append(num)

print(solve(*x))






def solve(*a):
    sum=0
    for i in a:
        sum+=i
    return sum
    
x=[]   
while True:
    num = input("Enter a number : ")
    if(num=="q"):
        break

    else:
        x.append(int(num))
print(x)
print(solve(*x)) 



def solve(*a):
    sum=0
    for i in a:
        sum+=i
    return sum
    
x=[]   
while True:
    num = input("Enter a number : ")
    if(num=="q"):
        break

    else:
        x.append(int(num))
print(x)  #same but element gulo rint kore dekte jabe..
print(solve(*x)) 



def solve(*a):
    sum=0

    for i in a:
        sum+=i
    return sum
    
x=[]   
while True:
    num = input("Enter a number : ")
    if(num=="q"):
        break

    else:
        x.append(int(num))
        print(x)  ## same as previous but each element  jotober input nibo..totober list hisebe dekte prbo..


print(solve(*x)) 



#lamda function..   lamda function e variable er nm function er nm hisebe kj kore..
#anonymous function is  also called  lamda function..
foo1 = lambda a,b : a+b
print(foo1(2,3)) 


#recursion in python..
#je function nije nijeke call kore..
#loop na chailye.. function e lopp er mto cholbe..

while True:
    num = int(input("Enter a Number : "))
 
    def factorial(n):
        if n==0 or n==1:
            return 1
        else:
            return n*factorial(n-1)
        
    print(factorial(num))          
        
    is_continue = input('type yes to continue or no for exit ').lower()
        
    if(is_continue=="yes"):
        pass
    else:
        break
         


def factorial(n):
        if n==0 or n==1:
            return 1
        else:
            return n*factorial(n-1)
        
print(factorial(4))    



