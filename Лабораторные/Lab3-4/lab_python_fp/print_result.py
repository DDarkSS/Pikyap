# Здесь должна быть реализация декоратора

def print_result(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        if len(args) == 1:
            res = func(args)
        else:
            res = func()
        res_type = type(res)
        special_print = [list, dict]
        if res_type in special_print:
            if res_type == list:
                for i in res:
                    if type(i) == tuple:
                        print(*i)
                    else:
                        print(i)
            elif res_type == dict:
                for i,j in res.items():
                    print(i, j, sep = " = ")
        else:
            print(res)
        return res
    return wrapper
if __name__ == "__main__":
    @print_result
    def test_1():
        return 1


    @print_result
    def test_2():
        return 'iu5'


    @print_result
    def test_3():
        return {'a': 1, 'b': 2}


    @print_result
    def test_4():
        return [1, 2]


    if __name__ == '__main__':
        print('!!!!!!!!')
        test_1()
        test_2()
        test_3()
        test_4()