def f(x):
    if x <= -2:
        res = 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        res = -x / 2
    else:
        res = (x - 2) ** 2 + 1
    return(res)

print(f(4.5))
print(f(-4.5))
print(f(1))
