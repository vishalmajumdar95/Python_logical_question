

# ### ADD LIST ITEMS
a=[[1,2,3,4,5,6],[4],3,[2,3,1],7,9]
ab=[]
b=0
for i in a:
    if type(a)==type(i):
        for j in i:
            ab.append(j)
	        # b+=j
    else:
	    b+=i
print(ab,'\n')




# ### ODD PRIME EVEN
n=[663,377,9,83,36,23,91,87,74,74,93,29,484,849,84,54,958,53674]
print('\nmain list => ',n,'\n')
a=[]
b=[]
c=[]
for i in n:
    if i%2!=0:
        a.append(i)
        for j in range(2,i):
            if i%j==0:
                break
            elif i==j+1:
                b.append(i)
    else:
        c.append(i)
print("\nODD:-",a)
print("\nPRIME:-",b)
print("\nEVEN:-",c,'\n')



### TABLES
num=int(input("En a number:-"))
t=[]
for i in range(1,num+1):
    t.append(i)
    n=[]
    for j in range(1,11):
        n.append(i*j)
    t.append(n)
print("LIST OF TABLES UPTO",num,"IS:-",t)
print()



# # ### LOGIC
user_name=input("Enter your name => ")
letter=input("Enter a alphanumeric letter do you want add => ")
v=0
ab=""
for i in user_name:
    if v==len(user_name):
        ab+=i
    else:
        ab+=i+letter
    v+=1
print(ab)
print()



