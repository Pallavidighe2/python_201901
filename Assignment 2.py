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

# for i in range(0,5):
#     for j in range (0,5):
#         print("*",end="  ")
#     print("")

for i in range(0,5):
     for j in range(0,5):
        print(i%2,end="  ")



     print("")



