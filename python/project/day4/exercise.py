import random
def get_random_number(start,end, number):
    numbers = []
    for i in range(number):
        numbers.append(random.randint(start,end))
    return numbers

if __name__ == '__main__':
    print(get_random_number(50,100,20))


    