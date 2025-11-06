# a=10
# while(a==11):
#     print("this is wrong")
# else:
#     print("it is done")    

# b=10
# while(b==10):
#     print("this is wrong")
# else:
#     print("it is done")    
#eta hocce infinty loop et a ke keyboard interrupt diye execution off korte hoy...
#using keyboard shortcut..ctrl+c...

# a=1
# while(a<11):
#     print(a)
#     a+=1
# else:
#     print("this is done")

# m=1
# while True:
#     print(m) 

# m=1
# while False:
#     print(m)        

#break statement..
# a=1
# while(a<11):
#     print(a)
#     if(a==8):
#         break
# a+=1    

#continue statement..
# m=0
# while(m<11):
#     m+=1
#     if(m==5):
#         continue    
#     print(m)


while True:
    name = input("enter your name: ")
    age = input("enter your  age: ")
    subject = input("enter your subject: ")
    print(f'Hello My name is {name}, age is {age} & my subject is {subject}.')

    is_continue = input("Do you want to Continue ? Type Yes or No for Exit ").lower()

    if is_continue=="yes":
        pass
    elif is_continue=="no":
        break
 
 ## here in paas we  can also use continue...which is the use of continue and break statement..

while True:
    name = input("enter your name: ")
    age = input("enter your  age: ")
    subject = input("enter your subject: ")
    print(f'Hello My name is {name}, age is {age} & my subject is {subject}.')

    is_continue = input("Do you want to Continue ? Type Yes or No for Exit: ").lower()

    if is_continue=="yes":
        continue
    elif is_continue=="no":
        break
 
#then for loop...

for x in range(6):
    print(x)


for x in range(2,10):
    print(x)   

for i in range(2,20, 3):
    print(i)     


#range function...it can use with one parameter...two parameter...and as well as..three parameter..

# for loop in break..
for i in range(6):
    print(i)
    if(i==4): break
    else:
        print("loop finished") #ekhane.. else use kora mne...for er sunstament hisebe..likha..tai..prptekkbar execute korbe..

for i in range(6):
    print(i)
    if(i==4): break
else:
    print("loop finished")

for i in range(8):
    if(i==6): 
        break  
    print(i)  
else:
    print("loop finished")


    
for i in range(8):

    if(i==6): continue  
    print(i)  
else:
    print("loop finished")
    

# pass stament...   
for i in range(8):

    if(i==6): pass 
    print(i)  
else:
    print("loop finished") 

#nested loops..
fruits = [1,2,3,6]
apple=[4,5,6]
for x in fruits :  #outer loop..
    for y in apple: #inner loop...inner loop ekber cholabe.fr each iteration of outer loop..
        print(x,y) 
    

a = " i love bangladesh"
for i in a:
    print(i)

#creating a  namta ...

while True:
    a  = int(input("enter a number  "))
    for x in range(1,11):
       print(f'{a} X {x} = {x*a}')

    is_continue = input("Doy you want to continue ? type yes or no for Exit ").upper()

    if(is_continue=="YES"):
        pass
    elif is_continue=="NO":
        break
    else:
        print("Invalid input") #..eta kj korbe jokon  Doy you want to continue ? type yes or no for Exit ei line yes  or no charar onno kno kichu dile..


a = "i love bangladesh"

for i in range(len(a)):
        print(f"{i}  {a[i]}")   

x = "how are you"
x= (x.replace("o", " "))
print(x)
       
x = "how are you"
x= (x.replace("o", ""))
print(x)
              



   
