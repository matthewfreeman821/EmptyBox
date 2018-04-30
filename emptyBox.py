def emptyBox(height, width):

    #height = int(input('How tall would you like the box? '))
    #width = int(input('How wide would you like the box? '))

    i = 0

    while i < height:
        if i == 0:
            n = 0
            while n < width:
                print('*', end='')
                n = n + 1
            print()
        n = 0
        while i < height - 2:
            while n < width:
                if n == 0:
                    print('*', end='')
                elif n == width - 1:
                    print('*', end='')
                else:
                    print(' ', end='')
                n = n + 1
            i = i + 1
            n = 0
            print()
        i = i + 1
        if i == height:
            n = 0
            while n < width:
                print('*', end='')
                n = n + 1
            print()
    return height, width
