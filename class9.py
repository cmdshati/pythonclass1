
## cls and its object create kora..
# cls er  nm first okkor ..capital hobe..  abr samll o dewa jai..

class Car:
    x=10
    y= 12

    def my_func(self):
        return 10-20
            
car1 = Car()
print(car1.my_func())
print(car1.x)
print(car1.y)
print(car1.x+car1.y)

class car:
    brand="sei ekta "

    def __init__(self , name, age):
     self.name = name
     self.age= age

    def __init__(self, a, b):
        print(a+b)


car2 = car(12,23)
# audi =car("afroza", 23)

# print(audi.brand)
# print(audi.name)
# print(audi.age)

##inheritance..
class A:  ## parent class..
   x=10
   y=20

   def __init__(self, num1, num2):
     print (num1 + num2)

## chils class.. as b cls er vhetor A cls ke dukai dewa hoyce..
class B(A): 
    name="afroza"
    age=23

# class2= A()
class1 = B(10,12)
print(class1.name)
print(class1.x)
print(class1.age)

## parent cls e constructor create kore..seta ke child cls er  instance ba object diye run koracci..

#ploymorphism..
#smae function different cls e thakbe..kintu kj differemt..

class Car:
   def move(self):
      print("Drive")


class Boat:
   def move(self):
      print("sail")


class Plane:
   def move(self):
      print("fly")  

class Train:
   def move(self):
      print("Run")          

car1 = Car()
boat1 = Boat()
plane1= Plane()  
train1 = Train()

car1.move()
boat1.move()
plane1.move()
train1.move()

# tuple1 =(12,23, 445,78)
# for i in tuple1:
#    print(i) 

for i in (12,23,445,78):
   print(i)    

#samvhabe object gula ke..tuple kaare lihkhe dilam.

for i in (car1, boat1, plane1,train1):
   i.move()


##single line if - else..

# if 15>12:
#   a = " i am right"
# else:
#  a = "i am wrong"

# print(a)

a="i am right " if 15>12 else "i am wrong "
print(a)

## single line for loop..
# a =[]
# for i in range(1,11):
#    a.append(i)

# print(a)   


a=[i  for i in range(1,11)]
print(a)
    
## cls er vhetoor function gulo ke parameter bole..    





