import random
w=0
l=0
t=0
print('Welcome to Rock, Paper, Scissors Game')
while(1):
    r = int(random.randint(1, 3))
    print('\n',w,'win',l,'lose',t,'tie')
    up=int(input('Enter 1 for rock, 2 for paper, 3 for scissors, 4 for quit: '))
    if (up==1 and r==1):
        print('Rock', 'vs', 'Rock', 'Tie')
        t=t+1
    elif (up==2 and r==2):
        print('Paper','vs','Paper', 'Tie')
        t=t+1
    elif (up==3 and r==3):
        print('Scissors','vs','Scissors', 'Tie')
        t=t+1
    elif (up==1 and r==2):
        print('Rock','vs','Paper', 'Lose')
        l=l+1
    elif (up==3 and r==1):
        print('Scissors','vs','Rock', 'Lose')
        l=l+1
    elif (up==3 and r==2):
        print('Scissors','vs','Paper', 'Lose')
        l=l+1
    elif (up==1 and r==3):
        print('Rock','vs','Scissors', 'win')
        w=w+1
    elif (up == 2 and r == 1):
        print('Paper', 'vs', 'Rock', 'win')
        w = w + 1
    elif (up == 2 and r == 3):
        print('Paper', 'vs', 'Scissors', 'win')
        w = w + 1
    else:
        break

