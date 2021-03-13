# 打印20个从50到100之间的随机数
# for 循环方法
# import random
# def get_random_number(start,end, number):
#     numbers = []
#     for i in range(number):
#         numbers.append(random.randint(start,end))
#     return numbers

# if __name__ == '__main__':
#     print(get_random_number(50,100,20))

# while 循环
import random
def get_random_number(start,end,number):
    numbers = []
    while True:
        temps = random.randint(start,end)  #随机生成一个随机数
        # 判断这个随机数在不在numbers里
        if temps not in numbers:
            numbers.append(temps)
            if len(numbers) >= number:
                return numbers

if __name__ == '__main__':
    print(get_random_number(10,50,8))
    







# import random
# list01 = [11,22,33,44,55,66,77,88,99]
# random.shuffle(list01)
# print(list01)

    
    