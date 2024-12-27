import json
import sys

from cm_timer import cm_timer_1
from unique import Unique
from print_result import print_result
from gen_random import gen_random
# Сделаем другие необходимые импорты

path = "/Users/mikalbr/Documents/3 Sem/Парадигмы и конструкции языков программирования/Lab3-4/lab_python_fp/data_light.json"

with open(path) as f:
    all_job_list = []
    data = json.load(f)
    for dct in data:
        try:
            all_job_list.append(dct['job-name'])
        except:
            pass
    job_list = Unique(all_job_list, ignore_case=True).get_data()

def filter2(list, job_name = "программист"):
    new_list = []
    for job in list:
        if job[0:len(job_name)].lower() == job_name:
            new_list.append(job)
    return new_list
@print_result
def f1(arg):
    print(arg[0])
    return sorted(arg[0], key = lambda x: x.lower())

@print_result
def f2(arg):
    return list(filter(lambda string: string[0:11].lower() == 'программист',arg[0]))
'''    return filter2(arg[0])'''



@print_result
def f3(arg):
    return list(map(lambda string: string + " с опытом Python,", arg[0]))


@print_result
def f4(arg):
    Salaries = gen_random(len(arg[0]), 100000,200000)
    Salaries = list(map(lambda string: 'зарплата ' + str(string) + ' руб', Salaries))
    return list(zip(arg[0], Salaries))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(job_list))))
