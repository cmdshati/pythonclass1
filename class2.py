print('i love "Bangldesh"')

# upper and lower function
text1 = "i love bangladseh"
print(text1.lower())
print(text1.upper())
print(text1.capitalize())
print(text1.title())
print(text1.swapcase())

# slicing
print(text1[2:6])
print(text1[0:])

# string negative slicing...
print(text1[-16:-6])

# fimding index number of a strong
print(text1.index('b'))
print(text1.index('a'))

# index number finding using find function

print(text1.find('g'))
print(text1.index('b'))

# finding string length
print(len(text1))
# finding occurance
print(text1.count('a'))

# string repalcing
print(text1.replace('bangladseh','amercia'))

# sting spliting
text="amr nm jni na"
text1='amr-nm-jni-na'
# b= text.split()
# b=text1.split()
# print(b)
# print(b)

print(text.split())
# print(text.split(""))
print(text1.split("-"))

# string striping/trimming
a="       i love bangladesh      "
print(a.strip())

a='------i love bangladesh------'
print(a.strip('-'))

# f string
a = input("Enter your number:")
b= input("Enter your age:")
c=input("enter your designation: ")
print(f'my name is {a} , i am {b} years old & my designation is {c}')

# multiline string
a1 =''' i love 
bangladesh  and this is my homeland
'''
print(a1)

# escape sequence
print('it\'s a cat')
print('it\\s a cat')
print("its our new \n bangladesh")
print("its our new \tcountry")
print("its our     new country")

#  ek ghor porimar space komanor jnoo...
print("its our   \bnew country")

a = input("Enter your name:").title()
b= input("Enter your age:")
c=input("enter your designation: ").capitalize()
# c=input("enter your designation: ").upper()

print(f'my name is {a} , i am {b} years old & my designation is {c}')



a =("i love bangldesh").upper()
print(a)
x=a.split()
print(x)
print(len(x))

# finding total length of string without space

#a.split e kno kichu join korbe na..
a =("i love bangldesh")
print(len(a))
x1="".join(a.split())
print(x1)
print(len(x1))

#a.split e space koin korbe..
x2=" ".join(a.split())
print(x2)
print(len(x2))

#a.split e # hash join korbe..
x3="#".join(a.split())
print(x3)
print(len(x3))

s1 = " this-is-our-country"
print(len(s1))
s2 = "||".join(s1.split("-"))
print(s2)
print(len(s2))

# string concatenation
s1 ="i love"
s2="bangladesh"
print(s1,s2)
print(s1+s2)
print(s1+ " " + s2)

# jdi string er mjkhane kno kichu  add korte chai..
s1= "i love bangladesh"
# i want to add "the"  before bangaldesh
s2 = s1[0:7] +"the " +s1[7:]
print(s2)





