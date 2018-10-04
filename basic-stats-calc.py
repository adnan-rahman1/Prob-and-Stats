from math import sqrt

def calc_mean(x):
    total_sum = 0.0
    for i in range(x):
        t = float(input())
        l.append(t)
        total_sum += t
    
    return total_sum/x


def calc_var(l, mean):
    total_val = 0
    for i in range(len(l)):
        total_val += (l[i] - mean)**2

    return total_val/len(l)


l = []
x = int(input('Enter the length of the input vector: '))

mean = round(calc_mean(x), 2)
var = round(calc_var(l, mean), 2)
std = round(sqrt(var), 2)
coef_var = round((std/mean) * 100, 2)

print('Mean of vector x: {}'.format(mean))
print('Variance of vector x: {}'.format(var))
print('Standard Diviation of vector x: {}'.format(std))
print('Coefficient of veriantion of vector x: {}%'.format(coef_var))
