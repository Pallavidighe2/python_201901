"""
1 annonymous Lambda function
2 Iterator
3 generator
4 generator VS iterator
5 Recursive Function

"""

### lambda function :

'''
lambda object : operation/expression
map(lambda object: operation/expression,iterable object)

'''

# _add_func= lambda ele1, ele2,ele3 : (ele1+ele2)*ele3
# print(_add_func(3,2,1))

# _sq = list(map(lambda x: x*x , [1,2,3,4,5]))
# print(_sq)

### ITERATOR :

# class MyRange():
#     """
#     my range function

'''   
    def __init__(self,n):
        self.i=0
        self.n=n

    def __iter__(self):
        return self

    def next(self):
        if self.i<self.n:
            i=self.i
            self.i+=1
            # return i
        else:
            raise StopIteration()
data = MyRange(5)
print(data.next())
print(data.next())
print(data.next())
print(data.next())
print(data.next())

'''

### GENERATOR :

'''
def simple_generator():
    yield 1
    yield 2
    yield 3

for item in simple_generator():
    print(item)

# for item in range(1,4):
#     print(item)

'''

## factorial programm using generator

'''
def factorial(limit):
    output=1
    initial=1
    while initial <=limit:
        yield initial*output
        output,initial=initial*output,initial+1

for i in factorial(5):
    print(i)
    
'''

## prime number using generator:

#not working i have to try.
'''
def prime(limit):
    output = 1
    initial=1
    while initial <=limit:
        yield initial%2!=0
        output,initial=initial%2==0 ,initial+1


for i in prime(6):
    print(i)


for i in range(2,number):
    if number%i==0:
        return false
    return true

'''


### RECURSIVE FUNCTION :

def prime_recursive(start,limit):
    if start==limit:
        return
    flag = True
    for divider in range(2,start):
        if start % divider == 0:
            flag=False
            break
    if flag:
        print(F'{start} is prime.')
    prime_recursive(start+1,limit)

prime_recursive(2,15)







