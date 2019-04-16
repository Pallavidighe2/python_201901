""""
this is class 02 file
1 Varibale
2 Data type: integer, string,boolean,none
3 Data structure : We can store multiple data type and their relationship in string

"""

integer_variable =3

print(integer_variable,id(integer_variable),)

# string

string_variable ="This is my sinle line string"
string_variable_2= "This is my" \
                    "multi line string 01"
string_variable_03="""
afs
vgd
ajhdgh

"""
#
# print(string_variable)
# print(string_variable_2)
# print(string_variable_03)
#



#boolean
true_flag=True
false_flag=False



##None

none_variable=None
#
# print("string_variable_03 ",type(string_variable_03))
# print("true_flag",type(true_flag))
# print("none_variable",type(none_variable),id(none_variable))

a=""
print("a",type(a))

# Data Structure

# 1 List

# list_variable= [ 'Pallavi' ,'Jayshree',215445,325.125, 'Pallavi']
# print(list_variable)
#
# print(type(list_variable[0]),type(list_variable[1]), type(list_variable[2]),type(list_variable[3]))
#
# print(list_variable.index('Jayshree'))  # showing index value of jayshree in list
#
# print(len(list_variable))
# print(list_variable.count('Pallavi'))

integer_list=[5,2,7,3,9,8]
print(sorted(integer_list))
integer_list.sort(reverse=True)
print(integer_list)

list_nested=[
    "Pallavi",["samarthtech","certview",[25512,2884]]
]

print(list_nested[1][2][0])

list_nested_02=[
    ['test1',['test2','test3',['test4']],'test5',['test6','test7'],'test8',['test9',['test10']]]
]

print(list_nested_02)
print(list_nested_02[0][4])
print(list_nested_02[0][5][1][0])


"""
Assignment

1 create 5 variable for each data type
2 create 5 list variable with 3 elements like name,address,contact number



"""

