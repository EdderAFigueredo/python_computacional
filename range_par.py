par = range(0, 101, 2)

col = 1

for i in par:
    if (col<10):
        print(f'{i}\t', end="")
        col = col + 1
    else:
        print(i)
        col=1