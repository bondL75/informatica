
from math import *

def task1():
    x = float(input("введите x: "))
    y = float(input("введите y: "))
    z = float(input("введите z: "))

    a = (abs(x-1)**-1)-(abs(y)**-1) - (1 + (x**2)/2 + (y**2)/4)
    b = x * (tan(z)+5)

    print("a= {:.4f}, b= {:.4f}")


def task2():
    x = float(input("введите x: "))
    a = 2
    b = 2
    c = -5

    f = (x**a) + (b*x**1/3)/(c*x + a)

    print("f(x)= {:.4f}")


def task3():
    x = float(input("введите x: "))

    f = (sin(x) + cos(x))/(cos(x) - sin(x))*tan(x)

    print("f(x)= {:.4f}")


def task4():
    a = float(input("введите a: "))
    b = float(input("введите b: "))
    c = float(input("введите c: "))

    print("x= {:.4f}")


def task5():
    pass


def task6():
    V = float(input("введите объём шара: "))
    P = V*6/

task3()
