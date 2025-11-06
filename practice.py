# # for i in range(6):
# #     print(i)
# #     if(i==4):
# #         break
# #     else:
# #         print("loop finished")


# # for i in range(6):
# #     print(i)
# #     if(i==4):
# #          break
# # else:
# #     print("loop finished")    

# # for i in range(8):
# #     if(i==6): continue
# #     print(i)
# # else:
# #     print("loop finished")  

# # for i in range(8):
# #     print(i)
# #     if(i==6): continue
# #     else:
# #          print("loop finished")   

# # fruits = [1,2,3,4]
# # apple=[4,5,6]
# # for x in fruits:
# #     for y in apple:
# #         print(x,y)              

# # #mutliplication table..


# # while True:
# #     a = int(input("Enter a number : "))
# #     for i in range(1,11):
# #        print(f'{a} X {i}= {a*i}')
# #     #    print(f'{a} X {i} = {i*a}')

# #     is_continue = input("Do you want to continue ? Type yes or no for exit: ").upper()

# #     if(is_continue=="YES"):
# #         pass
# #     elif is_continue=="NO":
# #         break    
# #     else:
# #         print("Invalid input")


# # a = " i love bangladesh"

# # for i in  range(len(a)):
# #     print(f'{i}   {a[i]}')

# # str = "now i am  mane"
# # print(str.replace("m", ""))

# # print(str.replace("m", " "))

# # print(str.replace("m", "#"))


# while True:
#     m = int(input("Enter first number : "))
#     n = int(input("Enter second number: "))
#     operator = input("Enter a operator like + - / or *: ")

#     if(operator == "+"):
#         print(m+n)
#     elif(operator=="-"):
#         print(m-n)
#     elif(operator=="*"):
#         print(m*n)  
#     elif(operator=="/"):
#         if n==0:
#             print(f'Error in {n}')
#             break
#         else:
#           print(int(m/n))
         
#     else:
#         print("Invalid operator")   


# while True:
#     m = int(input("Enter first number : "))
#     n = int(input("Enter second number: "))
#     operator = input("Enter a operator like + - / or *: ")

#     if(operator == "+"):
#         print(m+n)
#     elif(operator=="-"):
#         print(m-n)
#     elif(operator=="*"):
#         print(m*n)  
#     elif(operator=="/"):
#         if n==0:
#             print(f'Error in {n}')
#             break
#         print(int(m/n))
         
#     else:
#         print("Invalid operator")  
# 

# list1 = ["apple", "bangladesh", 123, True, None]                
# list1 .append(True)
# print(list1)

# list1.insert(7, "ami")
# print(list1)

# print(list1.index("bangladesh"))
# print(list1.count(True))

# list1.pop(1)
# print(list1)

# list1.remove(True)
# print(list1)

# # print(list1.clear())
# # list1.clear()
# # print(list1)

# #copy list ..
# list2 = list1.copy()
# print(list2)

# #reverse list..
# list1.reverse()
# print(list1)

# a = [1,2,3]
# b = [4,5,6]
# a.extend(b)
# print(a)

# b.extend(a)
# print(b)

# list3 = [34,  76, 89, 56,90]
# list3.sort()
# print(list3)


# fruits = ["apple", "mango", "guava"]
# for x in fruits:
#     print(x , end=" ")

# str = " i love bangla"
# for i in str:
#     print(i)

# for i in range(len(str)):
#     print(i)

# # str1 = "Bangaldesh is my motherland"
# # for i in range(len(str1)):
# #     # print(index())    


# ## tuple
# tuple1 = ("apple", "apple", "tuple", 123, 1233, 34, 34)
# print(tuple1)

# print(tuple1.index("apple"))
# print(tuple1.count(34))

# for i in tuple1:
#     print(i)

# #type casting of tuple..
# lst = list(tuple1) 
# print(lst)

# lst.append("were")
# lst = tuple(lst)
# print(lst)

# for i in lst:
#     print(i)


# question 1 : tuple er string type element gulo  ke  separate list e rakha..
    

t2=(23, 34 ,"string", "apple")
x=[]

for i in t2:
    if(type(i)==str):
        x.append(i)

print(x) 

tpl = ("amiJni", "Oma", 23)
print(tpl)
x=[]

for i in tpl:
    if(type(i)==str):
        x.append(i)
print(x)  

#another method..
t1 = [True, None, 123, "string","int"]
for i in t1:
    if(isinstance(i, str)):
        print(i)

t3 = [34, 87, "jhj", 89]
x = []
for i in t3:
    if(isinstance(i, str)):
        x.append(i)
print(x)

a = [1,2,3,4]
b = ["a", 'b', 'c']
for i in a:
    for j in b:
        print(i,j)
        print(f'{i}.{j}')

print(chr(65))    

#same but using ASCII character..
for i in range(1,11):
    for j in range(97,100):
        print(f'{i}.{chr(j)}')

for i in range(65,97):
    print(chr(i))

x1 = (1, 2, "You", [23,34,45])
x1[3].append("ami")
x1[3].append(34)
print(x1)

x2 = ['ass', 56, 98, (23,45, "apple")]
l1 = list(x2[3])
print(l1)
l1.append("str")
l1.append(56)
print(l1)
x2.append(l1)
print(x2)

x2 = ['ass', 56, 98, (23,45, "apple")]
l1 = list(x2[3])
l1.append("str")
l1.append(56)

x2[3] = tuple(l1)
print(x2)


## dictionary..
dic1 = {"name":"afroza", "age":23,"subject":"cse", "sem":7, "CGPA":3.67 }
print(dic1)
print(dic1["subject"])
dic2 = {"num1": 23 , "num2":34, "num4":67}
print(dic2)
print(dic2.keys())
print(dic2.values())

cpy = dic1.copy()
print(cpy)

cpy = dic2.copy()
print(cpy)

dic1.update({"CGPA": 3.69})
print(dic1)

# dic2.clear()
# print(dic2)

# remove kora.
dic2.pop("num1")
print(dic2)

dic1.popitem()
print(dic1)


print(dic1.get("name"))
print(dic2["num2"])

print(dic2.items())



x = []
x.append("python")
x.append("java")
x.append("c++")
x.append("C")
x.append(34)
print(x)


str = "i love bangaldesh"
x =[]
for i in str:
    if(i=="a"):
        x.append(str.index(i))
print(x)   

str = "Ami bangal jani"
x = []
for i in range(len(str)):
    if(str[i]=="a" or str[i]=="A"):
        x.append(i)
print(x)        


dic = {"a":1, "b":2, "c":3}
dic["a"]=5  ## dictionary elemnet change..
print(dic)

dic["c"]= 34
print(dic)

del dic["b"]
print(dic)
