def grade(score):
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 70:
        return "合格"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"


print(grade(float(input("请输入一个分数："))))
