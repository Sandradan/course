
# continue是这次跳过循环
# break是到这次直接结束循环

# def  continue_num(num):
#     n = 0
#     while  n < num:
#         n += 1
#         if n == 5:
#             continue
#         else:
#             print("n:",n)


# if __name__ == '__main__':
#     num = input('请输入一个数：')
#     continue_num(10);
    
    



#练手  求三位数中最大的57的倍数
# if __name__ == '__main__':
#     for i in range(999,100,-1):
#         if i % 57 == 0:
#             print(i)
#             break



import math
def is_prime_number(num:int):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False

    return True
# 输入一个数字，判断是不是质数
if __name__ == '__main__':
    num = int(input('请输入一个数：'))
    is_prime = is_prime_number(num)
    print(is_prime)
    
    
    