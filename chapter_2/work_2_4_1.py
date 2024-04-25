import math
import itertools

CONSTANT_h = 1.05460 * 10 ** -34
CONSTANT_e = 1.60219 * 10 ** -19
CONSTANT_m = 9.10938 * 10 ** -31


def list_J(L, S):
    start = L + S
    end = L - S
    return list(range(start, abs(end) - 1, -1))


def g_function(x, a, b):
    return 1 + ((x * (x + 1) - a * (a + 1) - b * (b + 1)) / (2 * x * (x + 1)))


def P_J_function(x):
    return CONSTANT_h * math.sqrt(x * (x + 1))


def MIU_J_function(x, y):
    return CONSTANT_e * x * y / (2 * CONSTANT_m)


def outcome(L, S):
    repeat_L = itertools.repeat(L)
    repeat_S = itertools.repeat(S)
    J = list_J(L, S)
    g = list(map(g_function, J, repeat_L, repeat_S))
    P_J = list(map(P_J_function, J))
    MIU_J = list(map(MIU_J_function, J, g))
    print("L=" + str(L), "S=" + str(S), "J=", J, "g=", g, "P_J=", P_J, "MIU_J=", MIU_J)


print("请输入L和S的值：")
L = int(input())
S = int(input())
outcome(L, S)
