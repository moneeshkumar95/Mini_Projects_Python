def listTostring(someList):
    a = ''
    for i in range(len(someList)-1):
        a += str(someList[i]+', ')
    a += str('and ' + someList[len(someList)-1])
    print (a)
spam = ['apples', 'bananas', 'tofu', 'cats']
listTostring(spam)