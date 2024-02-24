def swap_variables(a, b):

    a, b = b, a
    print(f" After Swapping: a: {a}  b: {b}")


if __name__ == '__main__':
    x, y = 10, 20
    print(f" Before Swapping: x: {x}  y: {y}")
    swap_variables(x, y)

