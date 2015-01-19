def seq3np1(n):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1."""
    count = 0

    while n != 1:
        count += 1
        # print(n)
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    # print(n)                  # the last print is 1
    return(count)

for i in range(1, 51):
    print "%d: %d," % (i, seq3np1(i)),