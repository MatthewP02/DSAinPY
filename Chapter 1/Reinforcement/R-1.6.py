#same function as R-1.4, but we add check that it is odd number
def sumOfSquares(n):
    x = [i*i for i in range(1, n) if i % 2 == 1]
    return sum(x)

#returns 35
print(sumOfSquares(6))