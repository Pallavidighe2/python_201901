""""
1 Data Structure: Dictionary, Tuple , Set

Assignment
1 create dictionary of user data
2 create list of user data dictionary with min of 10 user data
3 create dictionary which have list values
"""
# []= list
# {}= dictionary
# ()= tuple
dictionary_variable = {"name":"Pallavi"
    ,"address":"tansidh_samruddhi"
    ,"mobile number":9975881339

}

# print(dictionary_variable)
# print(dictionary_variable["name"])
# print(dictionary_variable.get("name"))
# print(dictionary_variable.get("contact no" , "Key not found"))
# print(dictionary_variable.keys())
# print(dictionary_variable.values())
# print(dictionary_variable.items())

# contact_no=dictionary_variable["mobile number"]
# print(dictionary_variable.pop("mobile number"))
# print(dictionary_variable)
# dictionary_variable["contact_no"]=9975884555
# print(dictionary_variable)

dict_01 =[{"test1":"test2","test3":"test4"},
          {"test5":[
          {"test6":"test7","test8":"test9"},
          {"test10":"test11","test12":"test13"}
          ]
}
]
# print(dict_01)
# print(dict_01[1]["test5"][1]["test12"])

dict_02={
    "test1":"test2","test3":[
        {"test4":"test5","test6":["test7","test8"]},
        [{"test9":"test10"},"test11",
         {"test12":"test13","test14":"Print_me"}],
        {"test15":"print_me2"}
    ]
}

# print(dict_02)
print(dict_02["test3"][1][2]["test14"])
print(dict_02["test3"][2]["test15"])


# a=[1,2,3,4,5,6,7,8]
# print(a[2:7])

tuple=(1,None)
print(tuple[1])