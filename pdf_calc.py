import numpy as np
import matplotlib.pyplot as plt

# Probability Density Function Calculator

x = int(input('Enter the length of the input vector x: '))

l = np.array([])

for i in range(x):
    t = float(input())
    l = np.append(l, t)

mean = l.mean()
std = l.std()


numerator = np.exp(-0.5 * ((l-mean)/std)**2)
denominator = std * np.sqrt(2*np.pi)

pdf = numerator / denominator

print('Probability density function of each X: ')
for i in range(len(pdf)):
    print('x = {} - pdf({}) = {}'.format(l[i], l[i], round(pdf[i], 5)))


plt.plot(l, pdf)
plt.show()
