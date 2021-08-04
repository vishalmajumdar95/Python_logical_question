def bodmas(list1): 
    while '/' in list1: 
        ind=list1.index('/')
        answer=list1[ind-1]/list1[ind+1]
        list1[ind-1:ind+2]=[answer]
    while 'x' in list1:  
        ind=list1.index('x')
        answer=list1[ind-1]*list1[ind+1]
        list1[ind-1:ind+2]=[answer]
    while '+' in list1: 
        ind=list1.index('+')
        answer=list1[ind-1]+list1[ind+1]
        list1[ind-1:ind+2]=[answer]
    while '-' in list1: 
        ind=list1.index('-')
        answer=list1[ind-1]-list1[ind+1]
        list1[ind-1:ind+2]=[answer]
    return list1

def bodmas_2():
        num=input("Enter expression : ")
        list1=[]
        string=''
        for i in num:
            if i.isdigit() or i=='.':
                string+=i
            elif i in ['/','+','-','x','(',')']:
                if string!='':
                    list1.append(float(string))
                if i=='(':
                    if isinstance(list1[-1],float):
                        list1.append('x')
                string=''
                list1.append(i)
        if string!='':
            list1.append(float(string))
        while '(' in list1: 
            close_brack = list1.index(')') 
            open_brack = len(list1)-list1[::-1].index('(')-1 
            new_list=list1[open_brack+1:close_brack]
            answer=bodmas(new_list) 
            list1[open_brack:close_brack+1]=answer 
        final_answer=(bodmas(list1))[0] 
        print(final_answer, 'is the final answer')
        return final_answer
bodmas_2()



