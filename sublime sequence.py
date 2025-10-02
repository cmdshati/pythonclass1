
t=int(input())
while t>0:
    p,q, r,s=map(int, input().split())
    
            
    if p==r and q==s:
        print("0")
    else:
        print(int(s/2))   
t-=1