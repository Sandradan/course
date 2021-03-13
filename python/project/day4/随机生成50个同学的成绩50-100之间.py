# 班级有50个同学，每个同学有5门课，随机生成50个同学的成绩（成绩介于50-100之间） 

# list = [
#     [43,66,65,4,78],
#     [43,66,65,4,78],
#     [43,66,65,4,78],
#     [43,66,65,4,78],
#    ...
# ]
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
def get_class_result(total_number:int):
    results = []
    for index in range(total_number):
        results.append(get_random_number(50,100,5))
    return results
if __name__ == '__main__':
    print(get_class_result(50))