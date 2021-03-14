def read_file_one(path:str):
    # 定义一个集合
    student = []
    try:
        #使用with打开文件
        with open(path, mode = 'r', encoding='UTF-8') as fd:
            #读取
            str01 = fd.read()# 一次读取整个文件
        print(str01)
    except Exception as e:
        print(str(e))
if __name__ == '__main__':
    path = r"D:\Sandra\course\python\project\day5\student.csv"
    read_file_one(path)
    