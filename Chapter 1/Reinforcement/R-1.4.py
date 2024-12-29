#x becomes a list of all squares < n, and we return the sum of the list
def sumOfSquares(n):
    x = [i*i for i in range(1, n)]
    return sum(x)

#returns 30
print(sumOfSquares(5))