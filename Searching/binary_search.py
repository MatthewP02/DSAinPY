import random

list = sorted([random.randint(1,100) for _ in range(50)])
find = 45
#randomized
print(list)
print(f"Need to find: {find}")

low = 0
high = len(list) - 1

while low <= high:
    mid = low + (high - low) // 2

    if list[mid] == find:
        print(f"Index for item {find} is {mid}")
        break
    if list[mid] < find:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Item not found inside list")