def list(spam):
    for i in range(len(spam)-1):
        print(spam[i], end=', ')
    print('and',spam[-1])
spam=['Apple','Bannana','Tofu','Cat']
list(spam)
