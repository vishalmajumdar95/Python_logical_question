##############-----> Nested list question first solution <-------############### 

main_list=[]
num_list=int(input("Enter how many indexes you want in main list => "))
counter=0
for i in range(num_list):
    sub_list=[]
    num_items=int(input("Enter how many indexes you want in sub list => "))
    if num_items==0:
        items=input("Enter your input => ")
        if items.isdigit():
            main_list.insert(counter,int(items))
            counter+=1
            continue
        else:
            main_list.insert(counter,items)
            counter+=1
            continue
    else:
        for j in range(num_list):
            items=input("Enter a index => ")
            if items.isdigit():
                sub_list.append(int(items))
            elif '.' in items:
                sub_list.append(float(items))
            else:
                sub_list.append(items)
    counter+=1
    main_list.append(sub_list)
print("\n\nFinal List => ",main_list,'\n\n')


##############-----> Nested list question second solution <-------############### 

# number of list 
num_list=int(input("How many list you want: "))
# number of items
num_items=int(input("How many items you want to add in list: "))
# main list and counter
main_list,counter,=[],0
# this loop run on length of items
for i in range(num_items):
    # append a sub_list in main_list
    main_list.append([])
    # this loop append the items in sub_list
    for j in range(num_items):
        
        items=input("Enter your items: ")
        
        if items >="a" and items<="z" or items>="A" and items<="Z":
            main_list[counter].append(items)
        
        elif items in "1234567890":
            items=int(items)
            main_list[counter].append(items)
            
        else:
            items=float(items)
            main_list[counter].append(items)
    counter+=1
print("\n\n Final list => ",main_list,"\n\n")

