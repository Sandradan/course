def read_file_one(path:str):
    # 定义一个集合
    students = []
    try:
        #使用with打开文件
        with open(path, mode = 'r', encoding='UTF-8') as fd:
            #读取
            # str01 = fd.read()# 一次读取整个文件，只针对小文件
            # str01 = fd.readlines() #也是一次性读取整个文件，返回值是list，每行都是list
            one_line = fd.readline() #一次只读取一行，识别到\n \n\t就结束
            while one_line:
                first_line = one_line.strip().split(',')
                students.append(first_line)
                one_line = fd.readline()
                
    except Exception as e:
        print(str(e))
if __name__ == '__main__':
    path = r"D:\Sandra\course\python\project\day5\student.csv"
    list01 = read_file_one(path)
    print(list01)