######### => FLATTEN LIST <= ##########

user_list=[1,2,3,5,333,[['Majum'],33,55,"n"],7,[5,[6,9,9,[6,["Vishal",[6,"sanju"]]]]]]
print('Main list => ', user_list,'\n')
for i in range(len(user_list)):
    for i in user_list:
        if type(i)==list:
            user_list.remove(i)
            for j in i:
                user_list.append(j)
print('\n',user_list,'\n')
