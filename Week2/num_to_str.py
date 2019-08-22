from functools import reduce

numlst = [1,4, 17, 0, -5]

print(reduce(lambda x, y: x * y, range(1, 6)))
