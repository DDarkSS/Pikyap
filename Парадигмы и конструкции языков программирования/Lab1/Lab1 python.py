def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

def input_check(sp):
    if len(sp) != 3:
        return False
    for i in range(3):
        if not is_digit(sp[i]):
            return False
    return True

def discr_search(A, B, C):
    return B*B - 4 * A * C

def result_search(A, B, D):
    res1 = (-B + D**0.5) / 2 / A
    res2 = (-B - D**0.5) / 2 / A
    t = {res1, res2}
    return t
def solve_b2_equation(A, B, C):
    D = discr_search(A, B, C)
    if D < 0:
        return False
    else:
        ans = sorted(result_search(A, B, D))
        return ans
def check(A, B, C, x):
    print("check:", x*x*A +B*x+C, sep = "")

while True:
    inp = input().split(" ")
    if input_check(inp):
        A = float(inp[0])
        B = float(inp[1])
        C = float(inp[2])
        answer = solve_b2_equation(A, B, C)
        if not answer:
            print("Уравнение не имеет решений")
        else:
            for i in range(len(answer)):
                print("x",i + 1,":",sep = "" ,end =" ")
                print(answer[i], sep = " ")
#                check(A,B,C,answer[i])
        exit()
    else:
        print("Исходные данные неверны")
