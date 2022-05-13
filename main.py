# Linear Regression
# For numerical analysis we know,
# m = (x_mean * y_mean - xy_mean) / ((x_mean)^2 - (x_mean^2)_mean)
# c = (y-mean) - m * (x-mean)

import numpy as np
import matplotlib.pyplot as plt


def plot_regression_line(x, y, m, c):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="m", marker="o", s=30)

    # predicted response vector
    y_pred = c + m * x

    # plotting the regression line
    plt.plot(x, y_pred, color="g")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    # function to show plot
    plt.show()


data_set_x = []
data_set_y = []

x_sum = 0
y_sum = 0
xy_sum = 0
x_square_sum = 0

data_size = int(input("Enter data size: "))

np_x = np.array([])
np_y = np.array([])

for i in range(0, int(data_size)):
    x = int(input("Enter pizza size(inch): "))
    y = int(input("Enter pizza price: "))
    np_x = np.append(np_x, x)
    np_y = np.append(np_y, y)
    # print("np_x: ", np_x)
    # print("np_y: ", np_y)
    data_set_x.append(x)
    data_set_y.append(y)
    # For equation value
    x_sum += x
    y_sum += y
    xy_sum += x * y
    x_square_sum += x ** 2

x_mean = x_sum / data_size
y_mean = y_sum / data_size
xy_mean = xy_sum / data_size
x_mean_square = x_mean ** 2
x_square_mean = x_square_sum / data_size

try:
    m = ((x_mean * y_mean) - xy_mean) / (x_mean_square - x_square_mean)
except ZeroDivisionError:
    m = 0

c = y_mean - (m * x_mean)

m_final = "{:.2f}".format(m)
c_final = "{:.2f}".format(c)

if c >= 0:
    print(f"\nSo, the line equation for linear regression is: {m_final}x+{c_final}")
else:
    print(f"\nSo, the line equation for linear regression is: {m_final}x{c_final}")


predicted_mean = 0
original_mean = 0

for i in range(0, int(data_size)):
    predicted_mean += (m * data_set_x[i] + c - y_mean) ** 2
    original_mean += (data_set_y[i] - y_mean) ** 2

try:
    accuracy = (predicted_mean / original_mean) * 100
except ZeroDivisionError:
    accuracy = 0

print(f"\nSo R-Squared Value or Accuracy of our model is: {accuracy}%")

print("Guess a pizza price from pizza size(inch): Y/N")
s = input()
if s == "Y":
    guessed_num = int(input("Enter the size of pizza(inch): "))
    res = m * guessed_num + c
    print(f"Price of the pizza will be: {res}")
    np_x = np.append(np_x, guessed_num)
    np_y = np.append(np_y, res)

plot_regression_line(np_x, np_y, m, c)


# # Linear Regression
# # For numerical analysis we know,
# # m = (x_mean * y_mean - xy_mean) / ((x_mean)^2 - (x_mean^2)_mean)
# # c = (y-mean) - m * (x-mean)
# data_set_x = []
# data_set_y = []
#
# x_sum = 0
# y_sum = 0
# xy_sum = 0
# x_square_sum = 0
#
# data_size = int(input("Enter data size: "))
#
# for i in range(0, int(data_size)):
#     x = int(input("Enter pizza size(inch): "))
#     y = int(input("Enter pizza price: "))
#     data_set_x.append(x)
#     data_set_y.append(y)
#     # For equation value
#     x_sum += x
#     y_sum += y
#     xy_sum += x * y
#     x_square_sum += x ** 2
#
# x_mean = x_sum / data_size
# y_mean = y_sum / data_size
# xy_mean = xy_sum / data_size
# x_mean_square = x_mean ** 2
# x_square_mean = x_square_sum / data_size
#
# try:
#     m = ((x_mean * y_mean) - xy_mean) / (x_mean_square - x_square_mean)
# except ZeroDivisionError:
#     m = 0
#
# c = y_mean - (m * x_mean)
#
# m_final = "{:.2f}".format(m)
# c_final = "{:.2f}".format(c)
#
# if c >= 0:
#     print(f"\nSo, the line equation for linear regression is: {m_final}x+{c_final}")
# else:
#     print(f"\nSo, the line equation for linear regression is: {m_final}x{c_final}")
#
# predicted_mean = 0
# original_mean = 0
#
# for i in range(0, int(data_size)):
#     predicted_mean += (m * data_set_x[i] + c - y_mean) ** 2
#     original_mean += (data_set_y[i] - y_mean) ** 2
#
# try:
#     accuracy = (predicted_mean / original_mean) * 100
# except ZeroDivisionError:
#     accuracy = 0
#
# print(f"\nSo R-Squared Value or Accuracy of our model is: {accuracy}%")
#
# print("Guess a pizza price from pizza size(inch): Y/N")
# s = input()
# if s == "Y":
#     guessed_num = int(input("Enter the size of pizza(inch): "))
#     res = m * guessed_num + c
#     print(f"Price of the pizza will be: {res}")
