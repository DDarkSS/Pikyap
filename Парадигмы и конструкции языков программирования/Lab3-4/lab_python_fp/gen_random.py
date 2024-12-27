from random import randint
def gen_random(num_count, begin, end):
    lst = []
    for i in range(num_count):
        lst.append(randint(begin, end))
        print(lst[-1])
    print()
    return lst
if __name__ == "__main__":
    gen_random(5, 1, 3)