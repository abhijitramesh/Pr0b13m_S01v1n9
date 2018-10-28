p=int(input())#inputting a value
k=str(p)#assigning the value as string
if str(k.count('7')+k.count('4')).count('7')+str(k.count('7')+k.count('4')).count('4')==len(str(k.count('7')+k.count('4'))):#cheaking condition
    print("YES")
else:
    print("NO")
