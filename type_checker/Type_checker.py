###---> type_function <---####

a=input("Enter a Number:")
if a.isnumeric(): print(type(int(a)))
elif len(a)>2 and "." in a and not a.endswith(".") and not a.startswith("."): print(type(float(a)))
elif len(a)>1 and "j" in a: print(type(complex(a)))
else: print(type(str(a)))

###---> type_function <---####

def type_of(elem):
    try:
        elem+'h'
        print("< class - 'str' >")
        return 'str'
    except TypeError as err:
        z=str(err)
        if 'list' in z:
            print("< class - 'list' > ") 
            return 'list'
        elif 'tuple' in z:
            print("< class - 'tuple' > ") 
            return 'tuple'

        else:
            z=(z.split(':')[1]).split('and')[0]
            print(f"< class - {z} >")
            return z
d=11
x=type_of(d)
print(x)


# Readme.md
# # Type_Function_Python
# This is simple type function based on Error Handling in Python. I have just added few lines of code to find type of any data without using any inbuilt function.

# ## Requirements

# ### A Text Editor
# We need a text editor to edit the type_of.py file and enter the data in file only to check it's type.

# After editing the file type_of.py, we can run this code in Linux terminal to get output `python3 type_of.py`
