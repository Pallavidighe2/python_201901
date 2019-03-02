'''

1 Built in function : min,max,count,len,split,zip,types,sum,sorted
2 Built in modules : os,sys,re,datetime,glob,math,time

'''

_list = [1,2,3,4,100,5,6,7,8,9,45,1]

print(min(_list))
print(max(_list))
print(_list.count(1))
print(len(_list))
print("this is what you want to split".split(" "))

fields = ["name","number"]
values = ["Pallavi","9975881339"]

for fields,values in zip(fields,values):
    print(fields,values)


list1 = [1,"a",["test"],{"test3":"test4"}]

for i in list1:
    print(type(i),i)

print(sum(_list))
print(sorted(_list))


