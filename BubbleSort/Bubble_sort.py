####---->Bubble_sort with for loop<----####

lis=[100,3,78,2,8,8,43,98,34,31,5]
for i in range(len(lis)):
    for j in range(len(lis)-1):
        if lis[i]<lis[j]:
            lis[i],lis[j]=lis[j],lis[i]
print(lis)

####---->Bubble_sort with while loop<----####

list1=[11,2,3,4,4,786,2,2,122,27]
i=0
while (i<len(list1)-1):
	if list1[i]>list1[i+1]:
		list1[i],list1[i+1]=list1[i+1],list1[i]
		i=0
	else:
		i+=1
print(list1)

