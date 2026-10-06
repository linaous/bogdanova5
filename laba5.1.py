num=[]
n=int(input('кол-во целых чисел'))
print('числа(каждое с новой строки)')
for i in range(n):
    o=int(input())
    num.append(o)
kn=0
for i in num:
    if i<0:
        kn+=1
print(kn)

     


