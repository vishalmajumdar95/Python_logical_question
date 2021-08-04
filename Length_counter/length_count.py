###########count the string length with out loop#############
# a=input("enter your string: ")
string="vishal"
a=string[-1]
count=string.index(a)
print(count+1)


###########count the string length with for loop#############

###**methed_1***###
v1=input("enter you str:")
print(sum(1 for count in v1))

###**methed_2***###
v=input("enter your string: ")
c=0
for i in v:
    c+=1
print(c)

###########count the string length with while loop#############
###**methed_1***###

v=input("enter your string: ")
b=""
c=0
while v:
    b=b+v[c]
    c+=1
    if v==b:
        break
print(c)

###**methed_2***###
v=input("enter your string: ")
c=0
while v[c:]:
    c+=1
print(c)

###########count the digits length with while loop#############

num=int(input("check your len:>"))
count=0
while num>=1:
    num=num//10
    count+=1
print("count length",count)



#########----count the length of list-----###########

l = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
c=0
for i in l:
    c+=1
print ("length of the list is ",c,)

l = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
c=0
while l[c:]:
    c+=1
print ("length of the list is ",c,)
###################################

# n=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
# c=0
# for i in n:
#     if i>20 and i<40:
#         c+=1 
#         print(i)
# print(c)

######################
# a=input()
# a=list(a)
# count=0
# l=0
# while a:
# 	a.remove(a[l])
# 	count+=1
# print(count)