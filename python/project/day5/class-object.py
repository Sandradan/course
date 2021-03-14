PI = 3.14
class Round:
    def __init__(self,radius:float):
        self.radius = radius
        self.primeter = 0.0
        self.area = 0.0

    def get_primeter(self):
        self.primeter = 2 * PI *self.radius

    def get_area(self):
        self.area = PI * self.radius *self.radius

if __name__ == '__main__':
    obj1 = Round(10)
    obj1.get_primeter()
    