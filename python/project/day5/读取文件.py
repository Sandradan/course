# def read_file_one(path:str):
#     # 定义一个集合
#     students = []
#     try:
#         #使用with打开文件
#         with open(path, mode = 'r', encoding='GBK') as fd:
#             #读取
#             # str01 = fd.read()# 一次读取整个文件，只针对小文件
#             # str01 = fd.readlines() #也是一次性读取整个文件，返回值是list，每行都是list
#             one_line = fd.readline() #一次只读取一行，识别到\n \n\t就结束
#             while one_line:
#                 first_line = one_line.strip().split(",")
#                 students.append(first_line)
#                 one_line = fd.readline()

#     except Exception as e:
#         print(str(e))
#     return students
# if __name__ == '__main__':
#     path = r"D:\Sandra\course\python\project\day5\student.csv"
#     list01 = read_file_one(path)
#     print(list01)


def read_file_two(path: str, infos: list):

    # 读取文件，存储的格式为：[{},{},{},{}]
    # :param path:
    # :param infos:
    # :return:
    students = []
    try:
        with open(path, mode='r', encoding='GBK') as fd:
            one_line = fd.readline()
            while one_line:
                first_line = one_line.strip().split(',')
                one_line_dict = {}
                for index, value in enumerate(first_line):
                    one_line_dict[infos[index]] = value
                students.append(one_line_dict)
                one_line = fd.readline()

    except Exception as e:
        print('读取文件出现异常' + str(e))
    return students

if __name__ == '__main__':
    path = r"D:\Sandra\course\python\project\day5\student.csv"
    infos = ['name', 'sno', 'gender', 'score']
    list01 = read_file_two(path,infos)
    print(list01)
