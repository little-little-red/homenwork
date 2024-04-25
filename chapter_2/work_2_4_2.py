def inside_circle(a, b):
    return a ** 2 + b ** 2 <= 1


def coordinates(a, b, coord_list):
    if any(inside_circle(a - i, b - j) for i, j in coord_list):
        print("打中了！")
    else:
        print("未打中")


print('请输入设计弹着点')
x = float(input())
y = float(input())
coordinates(x, y, [(2, -2), (-2, 2), (2, 2), (-2, -2)])
