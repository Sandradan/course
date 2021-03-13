list01=[24,456,24,66,77,84,38,90,32]
# 遍历：把集合的所有的元素按照顺序读取一遍

# 读取出所有的偶数

# list集合的遍历常见的三种方式：
# 第一种：for in  取值
 
for val in list01:
    if val % 2 == 0:
        print(val)

# 好处：取值非常方便
# 坏处：只能读取，不能修改或删除

# 第二种：for in range()   #取索引
for index in range(len(list01)):
    if list01[index] % 2 == 0:
        print(list01[index])
# 好处：可以读，修改和删除
# 坏处：取值时相对麻烦

# 第三种：把第一种和第二种的优势集为一身
# 如果是3的倍数，就给666
for index, value in enumerate(list01):
    if value % 3 == 0:
        list01[index] = 666
        print(list01)
