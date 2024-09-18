# GEO1000 - Assignment 1
# Authors: Xinya Bi, Xu Wang
# Studentnumbers:6195350 ,6235379

from math import sqrt


def abc(a, b, c):
    dis = discriminant(a, b, c)
    if dis > 0:
        x1 = (-b + sqrt(dis)) / (2 * a)
        x2 = (-b - sqrt(dis)) / (2 * a)
        print(f"The roots of {a} x^2 + {b} x + {c} are:"
              f" x1 = {x1} and x2 = {x2}")
    elif dis == 0:
        x =  - b / (2 * a)
        print(f"The roots of {a} x^2 + {b} x + {c} are: "
              f"x = {x}")
    else:
        print(f"The roots of {a} x^2 + {b} x + {c} are: "
              f"not real")



def discriminant(a, b, c):
     dis = b ** 2 - 4 * a * c
     return dis


abc(2.0, 0.0, 0.0)
abc(1.0, 3.0, 2.0)
abc(3.0, 4.5, 9.0)
