import random


diceThrow = random.randrange(1,7)
diceThrow2 = random.randrange(1,7)

def function1 (diceT, diceT2):
    x = 0
    if diceT > diceT2:
        x = diceT
    elif diceT < diceT2:
        x = diceT2
    elif diceT == diceT2:
        x = "Tie"
    return x

y = function1(diceThrow,diceThrow2)

print ("You", '\t', "Me", '\t', "Winner",)
print ("-----", '\t', "-----", '\t', "-------")
for x1 in range (1):
    print (diceThrow, '\t', diceThrow2, '\t', y)

