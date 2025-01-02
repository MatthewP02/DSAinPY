import random

list = [random.randint(1, 100) for _ in range(25)]
random.shuffle(list)
#randomized
print(list)

for i in range(1, len(list)):
    #set j = 0 for first index, and last index for i = len(list) due to zero indexing
    j = i - 1

    # while j is in bounds, and the next item is less than the current
    while j >= 0 and list[j+1] < list[j]:
        # temporarily hold the next item
        temp = list[j + 1]

        #swap the two elements to bring the smaller one to the left
        list[j + 1] = list[j]
        list[j] = temp

        #drop by one, and check if the item is smaller than the next (-1) item in the list
        j -= 1

#sorted
print(list)