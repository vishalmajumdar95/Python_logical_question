magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]] 
sum1,sum2,sum3,sum4=0,0,0,0
for j in magic_square:
    for i in range(len(magic_square)): sum1+=j[i]
for i in range(len(magic_square)): 
    for j in magic_square: sum2+=j[i]
    for k in range(len(magic_square)):
        if i==k: sum3+=magic_square[i][k]
        if i+k==2: sum4+=magic_square[i][k]
print("It is a Magic Square") if sum1//3==sum2//3==sum3==sum4 else print("It is not a Magic Square")


## Second way to check 
m = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
] 
a=0
b=0
c=0
d=0
v=len(m)
for i in range(v):
    for j in range(v):
        if i==j:
            a=a+m[i][j]
        elif i+j==3-1:
            b=b+m[i][j]
if a!=b:
    x=1
else:
    for i in m:
        c=0
        d=0
        for j in i:
            c=c+m[i][j]
            d=d+m[j][i]
        if d!=c:
            x=1
        elif d!=a:
            x=1
        else:
            x=0
if x==0:
    print("it is Magic Square")
else:
    print("it is not Magice Square")