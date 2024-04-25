import math


def calculate_roots(a, b, c):
    derta = b**2 - 4 * a * c
    if derta < 0:
        return None, None
    else:
        root1 = (-b + math.sqrt(derta)) / (2 * a)
        root2 = (-b - math.sqrt(derta)) / (2 * a)
        return root1, root2


while True:
    print("请输入二次方程的系数a, b和c：")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    root1, root2 = calculate_roots(a, b, c)
    if root1 is None and root2 is None:
        print("该二次方程没有实根。")
    else:
        print("二次方程的根是：", root1, "和", root2)

    continue_calculation = input("是否继续计算? (输入 'break' 以停止): ")
    if continue_calculation == "break":
        break
