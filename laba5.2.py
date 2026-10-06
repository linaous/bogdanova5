num=[]
n=int(input('кол-во целых чисел'))
print('числа(каждое с новой строки)')
for i in range(n):
    num.append(int(input()))
f=-1
for i in range(n):
    if num[i]<0:
        f=i
        break
l=-1
for i in range(n-1,-1,-1):
    if num[i]>0:
        l=i
        break
if f==-1:
    print('отрицательных нет')
elif l==-1:
    print('положительных нет')
else:
    s=0
    for i in range(f+1,l):
        s+=num[i]
    print(s)



