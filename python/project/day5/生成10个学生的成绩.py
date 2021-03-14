# 随机生成一个班的10个学生的信息，包含的信息有：学号、姓名、性别、班级和成绩明细,分数随机在50-100之间
# [
#
#     {"name":'mache','gender':'male','class':'senior01'，'result':[67,77,67,96,96]}，
#     {"name":'mache','gender':'male','class':'senior01'，'result':[67,77,67,96,96]}，
#     {"name":'mache','gender':'male','class':'senior01'，'result':[67,77,67,96,96]}，
#     {"name":'mache','gender':'male','class':'senior01'，'result':[67,77,67,96,96]}，
#     {"name":'mache','gender':'male','class':'senior01'，'result':[67,77,67,96,96]}，
#     {"name":'mache','gender':'male','class':'senior01'，'result':[67,77,67,96,96]}，
#     {"name":'mache','gender':'male','class':'senior01'，'result':[67,77,67,96,96]}，
#     {"name":'mache','gender':'male','class':'senior01'，'result':[67,77,67,96,96]}，
#     {"name":'mache','gender':'male','class':'senior01'，'result':[67,77,67,96,96]}，
#     {"name":'mache','gender':'male','class':'senior01'，'result':[67,77,67,96,96]}
#     
# ]


import random
names = ['mache', 'kidv', 'mary', 'dam', 'david',
         'tom', 'sabd', 'tony', 'dery', 'geen']
gender = ['male', 'female']
Class = 'senior01'
infos = ['sno', 'name', 'gender', 'class', 'result']

# 得到50-100之间的随机分数,有五门课的分数


# def get_random_number(start, end, number):
#     numbers = set()  # 定义一个集合存储分数
#     while len(numbers) < number:
#         numbers.add(random.randint(start, end))  # 生成随机数
#     return list(numbers)

# # 生成一个学生的成绩明细，拼成一个信息组

# # index学号，name姓名
# def get_onestudent_result(index: int, name: str):

#     # 根据list初始化一个dict
#     one_student_dict = {}.fromkeys(infos)
#     # 添加学号
#     if len(str(index)) == 1:
#         one_student_dict['sno'] = '9500' + str(index)
#     elif len(str(index)) == 2:
#         one_student_dict['sno'] = '950' + str(index)

#     one_student_dict['name'] = name
#     one_student_dict['gender'] = gender[random.randint(0, len(gender)-1)]
#     one_student_dict['class'] = 'senior01'
#     one_student_dict['result'] = get_random_number(50, 100, 5)
#     return one_student_dict

# def get_allstudent_result(number:int):
#     # 定义一个list存储所有的学生
#     all_students_result = []
#     for index,val in enumerate(names):
#         all_students_result.append(get_onestudent_result(index +1, val))
#     return all_students_result

# if __name__ == '__main__':
   
#     results = get_allstudent_result(10)
#     for i in results:
#         print(i)
    

#获取学生的分数result的值
def get_random_number(start, end, number):
    results = set()
    while len(results) < number:
        results.add(random.randint(start,end))
    return list(results)

# 拼接一个学生的成绩信息
def get_one(index:int, name:str):
    infos1 = {}.fromkeys(infos)
    infos1['name'] = name;
    infos1['sno'] = '9500' +str(index)
    infos1['gender'] = gender[random.randint(0,len(gender)-1)]
    infos1['class'] = 'senior01'
    infos1['result'] = get_random_number(50,100,5)
    return infos1


# 获取所有学生的信息
def all_students(number:int):
    allstudents_dict = []
    for i in range(number):
        allstudents_dict.append(get_one(i+1, names[i]))
    return allstudents_dict
    # for i,val in enumerate(names):
    #     allstudents_dict.append(get_one(str(i+1),val))
    # return allstudents_dict

if __name__ == '__main__':
    res = all_students(10)
    for i in res:
        print(i)

    
    


