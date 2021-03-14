import random
def get_random_number(start,end,number):
    set01 = set()
    while len(set01) < number:
        set01.add(random.randint(start, end))
    return set01

if __name__ == '__main__':
    result = get_random_number(50,100,10)
    print(result)