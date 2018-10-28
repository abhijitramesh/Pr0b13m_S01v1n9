import math
n,m=input().split()#splliting the input into two
n,m=int(n),int(m)#assigining the spllited input into two varables
count=0
a=list(map(int,input().split()))#assiging input as a list
for i in range(n-1):
    if a[i]>=a[i+1]:   
           count+=math.ceil(((a[i]-a[i+1])+1)/m)
           a[i+1]+=m*math.ceil(((a[i]-a[i+1])+1)/m)        
print(count)            
    
