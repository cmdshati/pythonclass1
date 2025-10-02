# while True:
#     num = int(input("Enter a Number : "))
 
#     def factorial(n):
#         if n==0 or n==1:
#             return 1
#         else:
#             return n*factorial(n-1)
        
#     print(factorial(num))          
        
#     is_continue = input('type yes to continue or no for exit ').lower()
        
#     if(is_continue=="yes"):
#         pass
#     else:
#         break
         
# def factorial(n):
#         if n==0 or n==1:
#             return 1
#         else:
#             return n*factorial(n-1)
        
# print(factorial(4))           



## file and exception handling...

# a = open("D:\\pythonfile.txt " , 'r')
# print(a.read())
# a.close()


# #file write .. .. 
# #eketre..a. write diye jeta likbo..oita file e write hoye jbe..kintu ager sn muche jbe..
# # ar jdi terminal e print kore dektace chai..tahoe read mode lgbe..
# a = open("D:\\pythonfile.txt " , 'w')
# a.write("I ami jni na ami jni")
# # a=open("D:\\pythonfile.txt " , 'r')
# # print(a.read())
# # a.close()
# ## append mode..last e append kore..
# a = open("D:\\pythonfile.txt " , 'a')
# a.write("ami kichu jni")
# #create mode .. 'x' ..
# #jdi amr  dewa location e kno file exist na kore tahole create mode ekta notun kore file create korbe..
# #ekber 'x' mode diye file create hole   again run korle  fileexits error dekabe.. as create mode ekber o new kore file create kore...
# a = open("D:\\pythonfile.txt " , 'w')
# a.write("I ami jni na ami jni")


## try and exception exception handling..

# a = int(input("Enter a number : "))
# for i in range(1,11):
#     print(f'{a} X {i} = {a*i}')

# b= "Motherland"    
# print(len(b))
# print(b.lower())
# print(b.upper())

# try:
#     a = int(input("Enter a number : "))
#     for i in range(1,11):
#         print(f'{a} X {i} = {a*i}')
# except: 
#    print("Invalid input")
# b= "Motherland"    
# print(len(b))
# print(b.lower())
# print(b.upper())



# try:
#     a = int(input("Enter a number : "))
#     for i in range(1,11):
#         print(f'{a} X {i} = {a*i}')
# except: 
#    pass
# b= "Motherland"    
# print(len(b))
# print(b.lower())
# print(b.upper())


##error ta ke print korate chaile 
# try:
#     a = int(input("Enter a number : "))
#     for i in range(1,11):
#         print(f'{a} X {i} = {a*i}')
# except Exception as e:
#     print(e)
  
# b= "Motherland"    
# print(len(b))
# print(b.lower())
# print(b.upper())


##try exception for divide by zero..


# try:
#     a= int(input("Enter a number : "))
#     b= int(input("Enter a second number:"))
#     ans =a/b
#     print(ans) 
# except:
#     print("not divide by zero.")       

##exceotion handling in file ...
# try:
#     c = open("D:\\pythonfile.tx",'w')
#     print(c.read())
# except:
#     pass  
# finally:
#     c.close()


# try:
#     c = open("D:\\pythonfile.tx",'r')
#     print(c.read())
# except:
#     print("file not found") 
# finally:
#     c.close()


# try:
#     a= int(input("Enter a number : "))
#     b= int(input("Enter a second number:"))
#     ans =a/b
#     print(ans) 
# except Exception as e:
#     print(e)     

# #using nested try except:
# try:
#     a = int(input("Enter a number : "))  # ei line e valid input na dile seta last excep  e chole jbe.. ar correct hole input niye right print korbe..
#     print("right")
#     try:
#         b= int(input("Enter another number: "))
#         ans = a/b
#     except Exception as e:
#         print(e)
# except Exception  as e:
#     print("Invalid Input !! Enter a number: ") 


# try:
#     c = open("D:\\pythonfile.tx",'w')
#     print(c.read())
# except Exception as e:
#     print("wrong")  #print(e)  
# finally:
#     c.close()                   

# try:
#     a = open("D:\\pythonfile.txt",'w')
#     a.write("I love Bangladesh")
#     try:
#         a = open("D:\\pythonfile.tx",'r')
#         print(a.read())
#     except  Exception as e:
#         print(e)
#     finally:
#         a.close() 
# except Exception as e:
#     print(e)  

#  ## same as input er mto...mne ager exampter mtoi..bujhar jonno ber ber print likhe dekhano hoyce..
#  ## ar  editor file location .tx diye vhul korleo dhorte prcete ..kintu sudu .t dile dhorte prce na..tokon outer try theke last except e chle jbe..
# try:
#     a = open("D:\\pythonfile.t")
#     # a.write("I love Bangladesh")
#     print("right")
#     try:
#         a = open("D:\\pythonfile.t",'r')
#         print(a.read())
#         print("read")
#     except  Exception as e:
#         print("something is wrong")
#     finally:
#         a.close() 
# except Exception as e:
#     print(" wrong")    

##kon error hooce seta print korchi.. e diye..

# try:
#     a = open("D:\\pythonfile.")
#     # a.write("I love Bangladesh")
#     print("right")
#     try:
#         a = open("D:\\pythonfile.t",'r')
#         print(a.read())
#         print("read")
#     except  Exception as e:
#         print(e)
#     finally:
#         a.close() 
# except Exception as e:
#     print(e)   

##file renaming ...
# file renaming er jonno os moudule use kora hoy..
# import os
# os.rename("D:\\file2.txt", "D:\\file3.txt")    

string = "i love bangladesh"                    

#finally block সবসময় execute হবে, exception হোক বা না হোক
#else block → তখনই execute হবে যখন exception occur না হয়

try:
    a= int(input("Enter a number : "))
    b= int(input("Enter a second number:"))
    ans =a/b
    print(ans) 
except Exception as e:
    print(e)  
else:
    print(f'final Output is : {ans}')   
    print("Else block is printed when exception si not occured")   

import my_module
def my_func(p,q):
    return p+q

print(my_func(my_module.a, my_module.b))

m=10
n=20


for  i  in range(1,11):
    print(i)

name="khanam"    