############# removing duplicated from list ###################

test_list = [1, 3, 5, 6, 3, 5, 6, 1, 1, 1, 2, 2, 2, 3]
print("The original list is : ",test_list)
# using naive method# to remove duplicated# from list

res = []
for i in test_list:
    if i not in res:
        res.append(i)

# printing list after removal
print("\nThe list after removing duplicates : ",res,'\n')


###########=> Second mothed to remove duplicate in <=#########


# removing duplicated from list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : " + str(test_list))
# using set()
# to remove duplicated
# from list
test_list = list(set(test_list))

# printing list after removal
print ("\n\nThe list after removing duplicates : " + str(test_list),'\n\n')
