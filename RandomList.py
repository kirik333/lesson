def RandomList(n,a,b):
    import random
    w = []
    while n>0:
        w.append(random.randint(a,b))
        n-=1
    return w
