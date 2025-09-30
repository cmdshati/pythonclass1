#arithmetic operators
a=10
b=20
print(a+b)
#modulus of a & b
print(a%b)

print(4**2)
print(97/2)
print(97//2)

#assignment operator
# = , +=, -+,*=,/=, %=, **=, //=, &=, |=,^=,>>=,<<=,:=

#comparison operator
# ==, !=,<=, >=,  <, >

a=10
b=20
print(a!=b)
print(a<b)
print(a>b)
print(a==b)

#logical operator
# ....and or not 

x=5
y=8
print(x<y and x==y)
print(x<y or x==y)
z=x<y or x==y
print(not z)
print(not (z))


#identity operators
#is .. is not
#it is  mainly used when  anyone sure that the answer is right.. and there is no reason  for comparison...
#like in the user account login system..we used for varification  password...
a1=10
b1=20
print(a1 is b1)
print(a1 is not b1)

#Menmbership opertaor..
#in , not in...only two is the member ship operator..

str ="i love in bangladesh"
print("b" in str)
print("A" not in str)

#bitwise operator..
# & | ~ >> << ^ ...^ eta hocce x-or ...
#0=0000
#  1=0001
# 2=0010
# 3=0011
# 4=0100
# 5=0101
# 6=0110
# 7=0111
# 8=1000
print(6 & 3)
print(6 | 3)
#x-or ..operator..
print(2^3)  #...even input hole zero..asbe..



#ASCII character..
print(chr(65))  #...capital A
print(chr(90))   #..capital Z

print(chr(97))  #small a...
print(chr(122))   #small...z

#using loop..
for i in range (65,91):
    # print(i , end=" ")
    print(chr(i) , end =" ")

print(end=" ")
#for small letter..
for i in range(97, 122):
    print(chr(i), end=" ")


#condition...if else ... elif(else if..)

p=20
q=78

if p<q :
    print("b is greater than a")
else:
    print("a is less tha b")  

#create a system that  will grade a  student  obtained marks..   
#make a calculator using if else  elif condition only...

marks = int(input("Enter a number"))

if( marks>=0 and marks<=100 ):

    if(marks>=80):
        print("A+")
    elif(marks>=70):
        print("A")
    elif(marks>=69):
        print("B")
    elif(marks>=40):
        print("C")
    elif(marks<30):
        print("Fail")   
else:
    print("invalid number")                

#this is the use of nested if else..


# lets  create a calculator...
while True:
    m = int(input("Enter first number : "))
    n = int(input("Enter second number: "))
    operator = input("Enter a operator like + - / or *: ")

    if(operator == "+"):
        print(m+n)
    elif(operator=="-"):
        print(m-n)
    elif(operator=="*"):
        print(m*n)  
    elif(operator=="/"):
        if n==0:
            print("Error in b")
            break
        print(m/n)
         
    else:
        print("Invalid operator")    
