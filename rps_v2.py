import random
w=0
l=0
t=0
print('Welcome to Rock, Paper, Scissors Game')
while(1):
    rsp=['rock','paper','scissors']
    r = str(random.choice(rsp))
    print('\n',w,'win',l,'lose',t,'tie')
    up=str(input('Enter rock, paper, scissors, or quit: '))
    if (up==r):
        print(r,'vs',up, 'Tie')
        t=t+1
    elif ((up=='rock' and r=='paper') or (up=='scissors' and r=='rock') or (up=='scissors' and r=='paper')):
        print(up,'vs',r, 'Lose')
        l=l+1
    elif ((up=='rock' and r=='scissors') or (up=='paper' and r=='rock') or (up=='paper' and r=='scissors')):
        print(up,'vs',r, 'win')
        w=w+1
    else:
        break

