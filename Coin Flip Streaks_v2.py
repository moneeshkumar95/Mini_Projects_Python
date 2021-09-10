import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    CoinFlip = [] #### (1) create a new, empty list for this list of 100
    for i in range(100):
        CoinFlip.append(random.randint(0,1))
    streak = 1 #### (2, 4) any flip is a streak of (at least) 1; reset for next check
    for i in range(1, len(CoinFlip)): #### (3) start at the second flip, as we will look back 1
        if CoinFlip[i] == CoinFlip[i-1]:  #checks if current list item is the same as before
            streak += 1
        else:
            streak = 0 #### (2) any flip is a streak of (at least) 1
        if streak == 6:
            numberOfStreaks += 1
            break #### (5) we've found a streak in this CoinFlip list, skip to next experiment
print(numberOfStreaks)