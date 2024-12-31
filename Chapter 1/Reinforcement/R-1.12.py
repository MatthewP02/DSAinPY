from random import randrange

#randomly select index from size selections
def choice(selections):
    return selections[randrange(0,len(selections))]

test = [1,23,8,6,3,1,25]
#returns random selection from test
print(choice(test))