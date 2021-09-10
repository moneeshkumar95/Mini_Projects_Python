import random
w=0
l=0
t=0
print('Welcome to Rock, Paper, Scissors Game')
while(1):
    r = int(random.randint(1, 3))
    print('\n',w,'win',l,'lose',t,'tie')
    up=int(input('Enter 1 for rock, 2 for paper, 3 for scissors, 4 for quit: '))
    if (up==r):
        print(r,'vs',up, 'Tie')
        t=t+1
    elif ((up==1 and r==2) or (up==3 and r==1) or (up==3 and r==2)):
        print(up,'vs',r, 'Lose')
        l=l+1
    elif ((up==1 and r==3) or (up==2 and r==1) or (up==2 and r==3)):
        print(up,'vs',r, 'win')
        w=w+1
    else:
        break

