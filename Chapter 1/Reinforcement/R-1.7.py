#formatted R-1.6.py to be on one line.
def returnSumOneLine(n):
    return sum([i*i for i in range(1, n) if i % 2 == 1])

#returns 35
print(returnSumOneLine(6))