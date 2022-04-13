# 矩阵相乘的reduce函数
import sys
import time
from mapper import n
from mapper import start_time
k=n # k表示矩阵A的列数
# 创建数据结构以保存当前行/列值
current_key = None
current_res = 0.0
value_dict = dict()

# 按行读取输入标准输入流（mapper.py）
for line in sys.stdin:
    #删除输入行首尾的空格
    line = line.strip()
    # 以‘\t’分割得到key和value
    key, value = line.split('\t',1)
    #解析键/值
    try:
        row, col = map(int, key.split(','))
        value = value.split(',')
        #key是矩阵相乘后矩阵C对应位置的行号和列号
        key = (row, col)
        replicate_key, element_value = int(value[1]), float(value[2])
    except:
        continue
    # 如果是在一样的key上...
    if key == current_key:
        #处理键/值对，reduce操作
        if replicate_key not in value_dict:
            value_dict[replicate_key] = [element_value]
        else:
            value_dict[replicate_key].append(element_value)
    # 如果key是下一个key，就计算C前一个key位置的值
    else:
        if current_key:
            #计算并输出结果到标准输出流
            for j in range(k):
                if (j in value_dict) and (len(value_dict[j]) == 2):
                    current_res += value_dict[j][0] * value_dict[j][1]
            #输出C的current_key位置的值
            print('{0},{1:f}'.format(current_key, current_res))
        #更新current_key、current_resd
        current_key = key
        value_dict = dict()
        #处理新的key
        value_dict[replicate_key] = [element_value]
        current_res = 0.0

#输出最后一个key的结果
if current_key:
    for j in range(k):
        if (j in value_dict) and (len(value_dict[j]) == 2):
            current_res += value_dict[j][0] * value_dict[j][1]
    print('{0} ,{1:f}'.format(current_key, current_res))
#输出程序运行时间
end_time = time.time()
sum_time = end_time - start_time
print("运行时间为%fs" %(end_time-start_time))