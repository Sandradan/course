# 统计各种字符的数量
if __name__ == '__main__':
    str = 'faFSHGSdgl23423nddfot你sd画的SDFA？？？“：》《》：{{：！@￥！nodgvcx'
    # 遍历每一个字符
    string = {"num":0,"upper":0,"lower":0,"chinese":0,"other":0}
    for char in str:
        if char.isupper():
            string["upper"] +=1
        elif char.islower():
            string["lower"] += 1
        elif char.isdigit():
            string["num"] += 1
        elif char>='\u4E00' and char <= '\u9FA5':
            string["chinese"] += 1
        else:
            string['other'] += 1
    print('大写字符：%d\n小写字符：%d\n数字字符：%d\n 汉字：%d\n其他：%d\n'%(string["upper"] ,string["lower"] ,string["num"] ,string["chinese"] ,string["other"] ))

            


