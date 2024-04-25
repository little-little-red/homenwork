CONSTANT_G = 6.67e-11


def fun_f(m_1, m_2, r):
    return CONSTANT_G * m_1 * m_2 / r**2


input_m_1 = float(input("请输入m_1的值："))
input_m_2 = float(input("请输入m_2的值："))
input_r = float(input("请输入r的值："))
print(fun_f(input_m_1, input_m_2, input_r))
# m_1 = 1e3 m_2 = 5.98e24 r = 3.8e4
