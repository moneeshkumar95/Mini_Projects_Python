def collatz(number):
    while number!=1:
        print(number)
        if number%2==0:
            number=number//2
        else:
            number = 3*number+1
    print(number)
ip=int(input("Enter the NUmber: "))
collatz(ip)


