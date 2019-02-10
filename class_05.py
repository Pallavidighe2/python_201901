"""
1 comprehension
2 user defined function

# ASSIGNMENT:
1 WRITE list comprehension to create 15 random number
2 write list comprehensioon to create prime number till user defined number
3 write dictionary comprehension with 5 key value paiir
4 convert all assignmnent into user defined function


"""


### COMPREHENSION:

# 1 LIST COMPREHENSION:

_odd = list()
# for i in range (1,10,2):
#     _odd.append(i)
# print(_odd)
#
#
# _odd=[i for i in range(1,10,2) ]
# print(_odd)

# for i in range (1,10):
#     if i%2==1:
#         _odd.append(i)
# print(_odd)

# _odd=[i for i in range(1,10) if i%2==1]
# print(_odd)

# 2 DICTIONARY COMPREHENSION:

# sq={}
#
# numbers=[2,4,6,8,8,10,3,5]
# for num in numbers :
#     sq[num]=num*num
# print(sq)
#
# _sq={ num:num*num for num in numbers}
# print(_sq)
#
# _sq={ num:num*num for num in numbers  if num%2==1}
# print(_sq)

labels = ["name", "age", "contact no"]
user1 = ["pallavi", 24, 9975881339]
user2 = ["sonali", 20, 9881942199]
user3 = ["poonam", 15, 874596312]

# output as :[{"name: "pallavi,"age":24,"contact no" :9975881339},
# { "name":"sonali","age":20, "contact no": 9881942199},
#  {"name":"poonam","age": 20,"contact no":874596312}
# ]


# labels1 = [{"name": user1[0] for i in user1}, {"age": user1[1] for i in user1}, {"contact no": user1[2] for i in user1}]
# print(labels1)
#
# label2=[ {"name":[0] for i in user1 }]


# output=[{label:user[index]for index,label in enumerate(labels)}
#         for user in [user1,user2,user3]]
# print(output)


# output=[{labels[index]:user[index] for index in range (0,3)}
#         for user in [user1,user2,user3]]
# print(output)



# op=list()
# for user in [user1,user2,user3]:
#     _user=dict()
#     for index in range(0,3):
#         _user[labels[index]]=user[index]
#     op.append(_user)
#
# print(op)



###2 USER DEFINED FUNCTION:

'''
## simple function

def<function name>():
    """
    function doc string
    """
    <statement1>
    <statement2>
    .
    .
    .
    <statementn>
    


'''

def greeting():
    print("Hello World")
# greeting()


def arg_greeting(name):
    """
    this is greeting function with argument
    :param name:
    :return:
    """

    print("hello {}".format(name))
    print(F"hello {name}")
# arg_greeting(name="parth")


def arg_return_greeeting(name):
    """
    this is greeting function with argument and return greeting message

    :param name:
    :return:
    """

    message=F"hello {name}"
    return message
# resp = arg_return_greeeting(name="pallavi")
# print(resp)

# name=input("enter your name : ")
# resp = arg_return_greeeting(name="pallavi")
# print(resp)


def wild_card_arg_greetings(*args):
    print(args)
    print(args[0],args[1])
wild_card_arg_greetings(*["test1","test2"])

def wild_card_kwargs_function(**kwargs):

    """


    :param kwargs:dictinary wild card argument
    :return:
    """

    for key, values in kwargs.items():
        print(key, ":", values)

user1={"name":"pallavi","age":24,"contact no":9975881339}
wild_card_kwargs_function(**user1)