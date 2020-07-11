import math


# ex2
def len_hypotenues_triangle(a, b):
    a = math.pow(float(a), 2.0)
    b = math.pow(float(b), 2.0)
    sum_a_b = a + b
    c = math.sqrt(sum_a_b)
    return '{:.4f}'.format(c)


if __name__ == '__main__':
    ex2 = len_hypotenues_triangle(2, 1)
    print(ex2)
