i=0
a=[]
# Take input form user 
while i<3:
    b=[]
    for j in range(3):
        j=int(input("Enter you namber:>"))
        b.append(j)
    a.append(b)
    i+=1
# print the Magic square box
print()
for i in range(3):
    for j in range(3):
        print(a[i][j],end=" ")
    # i+=1
    print()
# To check the table is magic square or not
s1=0
s2=0
for i in range(3):
    for j in range(3):
        if i==j:
            s1=s1+a[i][j]
        if i+j==3-1:
            s2=s2+a[i][j]
if s1!=s2:
    f=2
else:
    for i in range(3):
        s3=0
        s4=0
        for j in range(3):
            s3=s3+a[i][j]
            s4=s4+a[j][i]
        if s3!=s4:
            f=2
        elif s4!=s1:
            f=2
        else:
            f=1
if f==1:
    print("It is Magic square")
else:
    print("It is not Magic square")
