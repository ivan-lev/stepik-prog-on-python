def min(*a):
    m = a[0]
    for x in a:
        if m > x:
            m = x
    return m

print(min(5,3,6,-1,0,10,-3,6))
