#coding:utf-8
num=5
number=[0,1]
for i   in range(num):
    number.append(number[-2]+number[-1])
    print number
