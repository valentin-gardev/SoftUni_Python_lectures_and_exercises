height = int(input())
width = int(input())
for h in range(0, height):
    if h == 0 or h == height - 1:
        print('*' * width)
    else:
        for w in range(0, width):
            if w == 0:
                print('*', end='')
            elif w == width - 1:
                print('*')
            else:
                print(' ', end='')