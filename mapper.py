"""
利用mapreduce实现矩阵乘法
mapper.py :矩阵相乘的map函数
思路参考：
https://www.cnblogs.com/lytwajue/p/7399561.html
"""
import time
import numpy as np

#随机生成m*n的矩阵，每行的值为0-9的随机数
def generate_matrix(m,n):
    return np.random.randint(0,10,(m,n))

#m,n表示矩阵A的行数和列数，n,p表示矩阵B的行数和列数
m,n,p=10,10,10
#输入的矩阵A、B
A=generate_matrix(m,n)
B=generate_matrix(n,p)

#记录当前时间，单位为秒
start_time=time.time()

#分别遍历矩阵A和B，并进行map操作：
for row in range(len(A)):
    for col in range(len(A[0])):
        # 生成的键值对
        for k in range(p):
            print('{0:d},{1:d}\tA,{2:d},{3:f}'.format(row, k, col, A[row][col]))
for row in range(len(B)):
    for col in range(len(B[0])):
        # 生成的键值对
        for k in range(m):
            print('{0:d},{1:d}\tB,{2:d},{3:f}'.format(k, col, row, B[row][col]))
