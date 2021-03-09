# if 100:
#     print('判断正确')


# 输入某年某天，判断这个月有多少天
# 31: 1 3 5 7 8 10 12
# 30: 4 6 9 11
# 29: 2 可以被400整除或者（被4整除且不被100整除）
# 29：2

# 方法1
# if __name__ == '__main__':
#     year = int(input('输入的年份：'))
#     month = int(input('输入的月份：'))
#     day = 0
#     if month in [1,3,5,7,8,10,12]:
#         day = 31
#     elif month in [4,6,9,11]:
#         day = 30
#     else:
#         if (month == 2 )&(year % 400 == 0 or (year % 4 == 0 & year % 100 != 0)):
#             day = 29
#         else:
#             day = 28
#     print('%d年%d月:%d天'%(year,month,day))


# 方法2
if __name__ == '__main__':
    year = int(input('输入的年份：'))
    month = int(input('输入的月份：'))
    days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  
    if (month == 2)and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        day = days_list[month-1]+1
    else:
        day = days_list[month-1]
    print('%d年%d月:%d天' % (year, month, day))
