#sort data if it is not == 1, and return the last and first item as a tuple.
def minmax(data):
    if len(data) == 1:
        return (data[0], data[0])

    data.sort()
    return (data[0], data[-1])

#returns (1, 234)
print(minmax([3,56,7,8,32,3,1,234,6,4,2,1]))