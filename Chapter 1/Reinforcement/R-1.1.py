def is_multiple(num, divisor):
    #if there is remainder, return False
    #if no remainder, aka == 0, return True
    return num % divisor == 0

# Returns True
print(is_multiple(9, 3))