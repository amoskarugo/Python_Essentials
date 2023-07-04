def topten(n):
    for i in range(n):
        yield i

x = topten(10)

print(x.__next__())