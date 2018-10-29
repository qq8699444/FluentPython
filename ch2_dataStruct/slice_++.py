import os
from  collections import  namedtuple

## 2.4.1
l = [10,20,30,40,50,60]
print(l[:2])
print(l[2:])

print(l[:3])
print(l[3:])


## 2.4.2
s = 'bicycle'
print(s[::3])
print(s[::-1])
print(s[::-2])

## 2.4.4
l = list(range(10));    print(l)
l[2:5]  = [20,30];      print(l)
del l[5:7] ;            print(l)
l[3::2] = [11,22];      print(l)
l[2:5] = [100];         print(l)


## 2.5
l = [1,2,3]
print(l*5)
print(5*'abcd')

board = [['_']*3 for i in range(3)]
print(board);board[1][2] = 'X';print(board)

weird_board = [['_']*3]*3
print(weird_board);weird_board[1][2] = 'X';print(weird_board)


## 2.6
print(id(l));l *= 2;print(id(l))

t = (1,2,3)
print(id(t));t *= 2;print(id(t))


t = (1,2,[3,4])

t[2] += [5,6]


print(t)
