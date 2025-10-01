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

