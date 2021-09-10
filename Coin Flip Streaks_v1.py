import random #imported the random
numberofstreaks=0  #setting the numberofstreak = 0
for experimentnumber in range(10000):
    flip = ('')
    for i in range(100):
        if random.randint(0,1)==1:
            flip+='H'
        else:
            flip+='T'
    try:
        if (flip.index('HHHHHH')): # check for the head streak
            numberofstreaks+=1
        if (flip.index('TTTTTT')): # check for the tail streak
            numberofstreaks+=1
    except ValueError:
        numberofstreaks+=0
print('Chance of streak: %s%%' % (numberofstreaks / 100))


