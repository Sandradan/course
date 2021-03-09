PI = 3.14

def input_num():
    while True:
        radi_str = input("请输入半径：")
        try:
            radi = float(radi_str)
            return radi
        except:
            print('您输入的半径无效')

def get_area(radi: float):
    peri = radi*2*PI
    return peri

def get_peri(radi: float):
    area = PI*radi*radi
    return area

if __name__ == '__main__':
    radi_str = input_num()
    print("圆的周长为：%f" % get_area(radi_str))
    print("圆的面积为：%.2f " % get_peri(radi_str))
