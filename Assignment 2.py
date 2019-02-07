""""Assignments:
1) write a code to find maximum number from 5 values
2) write a code to find minimum number from 5 values
3) write a code to find maximum number from 10 values with only single if statement
4) write a code to find minimum number from 10 values with only single if statement
Create pattern using for or while loop
1)                  2)              3)                  4)
* * * * *           1 1 1 1 1       0 0 0 0 0           0
* * * * *           1 1 1 1 1       1 1 1 1 1           1 0
* * * * *           1 1 1 1 1       0 0 0 0 0           0 1 0
* * * * *           1 1 1 1 1       1 1 1 1 1           1 0 1 0
* * * * *           1 1 1 1 1       0 0 0 0 0           0 1 0 1 0
5)                  6)              7)                  8)
1                   1 2 3 4 5       01 02 03 04 05      1 0 1 0 1
1 0                 1 2 3 4 5       06 07 08 09 10      0 1 0 1
1 0 1               1 2 3 4 5       11 12 13 14 15      1 0 1
1 0 1 0             1 2 3 4 5       16 17 18 19 20      0 1
1 0 1 0 1           1 2 3 4 5       21 22 23 24 25      1
9)                  10)             11)                 12)
      1             * *   * *       01 02 03 04 05      2
   1    1           *  * *  *       05 04 03 02 01      2 4
  1   1   1         *   *   *       02 04 06 08 10      2 4 8
1   1   1   1       *       *       10 08 06 04 02      2 4 8 16
                    *       *       03 06 09 12 15      2 4 8 16 32
                                    15 12 09 06 03      2 4 8 16 32 64
13) *       *
    * *   * *
    *   *   *
    *       *
    *       *
1) Create a Matrix
2) Matrix Multiplication
3) Spiral Matrix rotation
4) Shift elements in Matrix

"""""

###1

"""
for i in range(5):
    for j in range (5):
        print("*",end=" ")
    print()
"""

###2
"""
for i in range (1,6):
    for j in range (5):
        print(int(i/i),end='  ')
    print()
"""

###3

"""
for i in range (5):
    for j in range (5):
        print(i%2, end ="  ")
    print()
    
"""

###4

"""
for i in range (6):
    for j in range(i):
        if ( i==1 or i==3 or i==5):
            print(j%2,end=" ")
        if (i==2 or i==4):
            print((j+1)%2,end=" ")
        # if i==3:
        #     print(j%2,end=" ")
        # if i==4:
        #     print((j+1)%2,end=" ")
        # if i==5:
        #     print(j%2,end= " ")
    print()

"""

###5
"""
for i in range (6):
    for j in range(1,i+1):
        print( j%2 ,end=" " )

    print()
"""

###6

"""
for i in range(5):
    for j in range(1,6):
        print(j,end =" ")
    print()
"""

###7(not getting 0 before single digit number)

"""
for i in range(1,6):
    for j in range(1,6):
        if i==1:
            print("0"+str(int(j)),end="  ")
        elif i==2:
            print(j+5,end="  ")
        elif i==3:
            print(j+10,end=" ")
        elif i==4:
            print(j+15,end=' ')
        elif i==5:
            print(j+20,end=" ")

    print()
"""

###8

"""
for i in range(5):
    for j in range(5-i):
        if (i==0 or i==2 or i==4):
            print(j%2,end=" ")
        elif (i==1 or i==3):
            print((j+1)%2,end=" ")
        # if i==2:
        #     print(j%2,end=" ")
        # elif i==3:
        #     print((j+1)%2,end=" ")
        # if i==4:
        #     print(j%2,end=" ")
        # else:
        #     print("*",end=" ")
    print()

    print(end="")
"""


###9

"""
for i in range(4):
    for j in range(7):
        if ((i==0 and j==3) or (i==1 and (j==2 or j==4)) or (i==2 and (j%2==1 )) or ( i==3 and (j%2==0))     ):
            print("1",end=" ")
        else:
            print(" ", end=" ")


    print()

"""



###10(not getting proper output)

"""
for i in range(5):
    for j in range(5):
        if (j==0 or j==4):
            print("*",end="")
        else:
            print("" ,end=" ")
        if (j==1 and(i<=1)):
            print("*",end="")
        else:
            print("" ,end=" ")

        if  ((j==3)and (i<=1)):
            print("*", end="")
        else:
            print("" ,end=" ")
        if (i==2 and j==2):
            print("*",end="")
        else:
            print("" ,end=" ")

    print()

"""

"""
for i in range(5):
    for j in range(5):
        if ((j==0 or j==4)or (j==1 and(i<=1))or ((j==3)and (i<=1))or (i==2 and j==2)):
            print("*",end="")
        else:
            print("" ,end=" ")
    print()
"""

###11(not getting output)

"""
for i in range(1,7):
    for j in range(1,6):
        if i==1:
            print(j,end=" ")
        if i==3:
            print(j*2,end=" ")
        if i==5:
            print(j*3,end=" ")
        if i==2:
            print()


    print()


"""


###12

for i in range(1,7):
    for j in range(1,i+1):
        print(2**j,end=" ")
    print()