# 输入第一个数：100
# 选择操作运算符（+ - * /  %)
# 输入第二个数：40
# 结果：60


if __name__ == "__main__":
    first_num = int(input('输入第一个数：'))
    sign = input('请输入操作运算符')
    second_num = int(input('输入第二个数：'))
    result = first_num+sign+second_num
    print('结果：%d'%result)