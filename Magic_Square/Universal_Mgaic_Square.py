num=int(input("enter how many rows and columns you want:"))
m=[]
for i in range(num):
    a=[]
    for j in range(num):
        b=int(input("enter the inputs:"))
        a.append(b)
    m.append(a)
print(m)
for i in range(len(m)):
    row=0
    col=0
    for j in range(len(m[i])):
        row+=m[i][j]
        col+=m[j][i]
    d1=0
    d2=0
    for k in range(len(m[i])):
        d1+=m[k][k]
        d2+=m[k][-k-1]
if row==col==d1==d2:
    print(m,"IT IS A MAGIC SQUARE")
else:
    print(m,"IT IS NOT A MAGIC SQUARE")