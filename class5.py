# list
# data type different nite prbo list e
# list = [23,23.80,'bangladesh', True,None]

# print(list[0])
# print(list[1:])
# print(list[-4:])
# print(list[-4:-1])

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
#             print("Error in b")
#             break
#         print(int(m/n))
         
#     else:
#         print("Invalid operator")    

#list..

# list1 = ["apple", "banana", 'lichi']
# print(list1)

#append method...
# list2 = [34, "bangladesh", True , None]
# list2 .append(False)
# print(list2)

#insert method..
list2 = [34, "bangladesh", True , None, 34, 34]
# list2 .insert(0,False)
print(list2)
#index ber kora..
# print(list2.index(34))
#item count..
# print(list2.count(34))

#item remove or delete from list..
# print(list2.pop(2))
# print(list2)

# #then using another method...
# list2.remove(34)
# print(list2)

#list clear kora..
# print(list2.clear())#...evhebe likel .output none dekabe..
# print(list2) # but evhabe likle output khali list dekabe..

# b= list2.copy()
# print(b)

#list reverse..
# list2.reverse()
# print(list2)

#extend  function...
# a= [1,2,3]
# b=[4,5,6]
# a.extend(b)
# print(a)

# print(b)

#anotherly..
# b.extend(a)
# print(b)


# a1=[23,54,67,89,45,1]
# a1.sort()
# print(a1)

# fruits = [23, 56, 78]
# for x in fruits:
#     print(x)


a = "i love"
for i in a: # its store single character of  a string..
    print(i)
for i in range(len(a)): # its store index of the string..
    print(i)


#string theke   character er index ber kora..
a= "i love bangladesh"
x=[]
for i in range(len(a)):
    if(a[i]=="a"):
        x.append(i)
        
print(x)

# another method..  but it doesnot work as index method always returns the first occurance of a character in a string..
a= "i love Bangladesh"
for i in a:
    if(i=="a"):
        print(a.index(i))

##
a= "i love bangladesh"
for i in range(len(a)):
    if(a[i]=="a"):
       print(i)


x=[]
x.append("python")
x.append("java") 
x.append("C") 
x.append("C++")
print(x)      


fruits=["apple", "lichi", "mango"]
#fruits.dot dile je  je method gulo asbe..segulo sb kora jai..list e..
##tuple..
tuple1=(23,34,4,5, "apple","apple")
print(tuple1)

print(tuple1.count("apple"))
print(tuple1.index(34))

#
for i in tuple1:
    print(i)

#tuple ke type cast kore list e chnage kore sb dhoroner rupanthor  kora jai..list er mto..

b= list(tuple1)
print(b)

b.append("apple")
print(b)
## list e item append korar por abr tuple e convert korla..
tuple1=tuple(b)
print(tuple1)

for i in tuple1:
    print(i)



t2=(23, 34 ,"string", "apple")
x=[]

for i in t2:
    if(type(i)==str):
        x.append(i)

print(x)  

##tuple er string type element gulo ke ekta list e rakha..
t2=(23, 34 ,"string", "apple")
x=[]

for i in t2:
    if(type(i)==str):
        x.append(i)

print(x) 

##another method..
t2=(23, 34 ,"string", "apple")


for i in t2:
    if(type(i)==str):
        print(i)

#using isinstance   function or method.. 
# t3=[34, 45, 67, 12 , "bangladesh", "india"]


# for i in t3:
#     if isinstance(i, str):
#         print(i)


t3=[34, 45, 67, 12 , "bangladesh", "india"]
y=[]

for i in t3:
    if isinstance(i, str):
        y.append(i)

print(y)   


##nested loop..
a=[1,2,3,4,5]
b=["a","b","c"]

for i in a:
    for j in b:
        print(f'{i}.{j}')


a=[1,2,3,4,5]
b=["a","b","c"]

for i in a:
    for j in b:
        print(i,j)        

#using  ASCII value..
for i  in range(1,10):
    for j in range(97,100):
        print(f'{i}.{chr(j)}') 
    
#ASCII  character print kora..
print(chr(65))    


#tuple er modde kno list thakle seta ke change kora jai..

a1=(2,3,45,[34,56,78])
a1[3].append("apple")
print(a1)


##dictionary...it s key value pair..

dic1 = {"name":"afroza", "age":23,"subject":'CSE'}
#print(dic1)
print(dic1["name"])
# sngual key pawa jbe..
print(dic1.keys())
# sbguula values pawa jbe..
print(dic1.values())
#cpoy kora..
d= dic1.copy()
print(d)

#clear kora..
# d.clear()
# print(d)

#update kora..
d.update({"CGPA":"344"})
print(d)


#remove kora..
d.pop("age")
print(d)

#another method..
d.popitem()
print(d)
#jdi kono ekta key er value chnage korte chai.. ba replace korte chai..
d.update({"name":"karim"})
print(d)


#get method..
print(d.get("name"))

#same as..
print(d["name"])

#items method..  key value pair gulo ke.. list er items hisebe rakhe..
print(d.items())