import math
import sys
def gamma(a, w, R, x=[]):
    out_sum = 0
    out_weight = 0
    for i in range(len(x)):
        out_sum += a[i] * x[i]
        out_weight += w[i] * x[i]
    for i in range(len(x),len(a)):
        if w[i] <= R - out_weight:
            out_weight += w[i]
            out_sum += a[i]
        elif R > out_weight:
            out_sum += a[i] * (R - out_weight) / w[i]
            out_weight += (R - out_weight) / w[i]
    if out_weight > R:
       out_sum = - math.inf
    return out_sum


def sort_1(a,w):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]/w[i] < a[j]/w[j]:
                a[i], w[i], a[j], w[j] = a[j], w[j], a[i], w[i]
    return a, w


def max_backpack(a, w, R, x=[]):
    if len(a) == len(x):
        return x

    x1 = [i for i in x]
    x2 = [i for i in x]
    x1.append(0)
    x2.append(1)
    gamma_x1 = gamma(a, w, R, x1)
    gamma_x2 = gamma(a, w, R, x2)

    if gamma_x1 > gamma_x2:
        record_x1 = max_backpack(a, w, R, x1)
        if gamma(a,w,R,record_x1) < gamma_x2:
            record_x2 = max_backpack(a, w, R, x2)
            if gamma(a,w,R,record_x2) > gamma(a,w,R,record_x1):
                record = record_x2
            else:
                record = record_x1
        else:
            record = record_x1
    elif gamma_x1 < gamma_x2:
        record_x2 = max_backpack(a, w, R, x2)
        if gamma(a, w, R, record_x2) < gamma_x1:
            record_x1 = max_backpack(a, w, R, x1)
            if gamma(a, w, R, record_x1) > gamma(a, w, R, record_x2):
                record = record_x1
            else:
                record = record_x2
        else:
            record = record_x2
    else:
        record_x1 = max_backpack(a, w, R, x1)
        record_x2 = max_backpack(a, w, R, x2)
        if gamma(a,w,R,record_x1) < gamma(a,w,R,record_x2):
            record = record_x2
        else:
            record = record_x1
    return record


def task(costs, weights, limit):
    costs, weights = sort_1(costs, weights)
    print("Входные данные: ")
    print(" ( max(",end="")
    for i in range(len(costs)):
        print(str(costs[i])+"x"+str(i+1),end="")
        if i < len(costs)-1:
            print("+", end="")
    print(");")
    print("<  ",end="")
    for i in range(len(weights)):
        print(str(weights[i])+"x"+str(i+1),end="")
        if i < len(weights)-1:
            print("+", end="")
    print(" <=",limit)
    print(" ( X1...X"+str(len(costs))+" из {0,1}")
    result = max_backpack(costs, weights, limit)
    max_cost = gamma(costs, weights, limit, result)
    result_string = " ".join(map(str, result))
    print("\nОтвет: ("+ result_string +")")
    print("Максимальная стоимость рюкзака:", max_cost)



a = [2, 4, 2, 5]
w = [4, 3, 5, 2]
R = 11
task(a,w,R)
