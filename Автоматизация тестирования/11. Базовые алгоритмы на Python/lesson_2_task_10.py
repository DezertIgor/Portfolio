def bank(x, y):
    for i in range(0, y):
        x = x * 1.1
    print(f'{x:.2f}')
bank(10, 5)
