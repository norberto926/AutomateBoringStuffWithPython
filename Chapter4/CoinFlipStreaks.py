import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    heads_or_tails = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            heads_or_tails.append("T")
        else:
            heads_or_tails.append("H")
            
    streak = 0       
    for i in range(1, len(heads_or_tails)): 
        if heads_or_tails[i] == heads_or_tails[i - 1]:
            streak += 1
            if streak == 6:
                numberOfStreaks += 1
                break
        else:
            streak = 0
            
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
           
            
            
            