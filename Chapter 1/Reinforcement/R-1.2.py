#loop, and toggle even to True or False, returning True if triggered even number of times, false otherwise
def is_even(k):
    if k == 0:
        return False
    
    even = True
    for i in range(k):
        even = not even
    return even

#returns false
print(is_even(1))

#returns false
print(is_even(5))

#returns true
print(is_even(12))