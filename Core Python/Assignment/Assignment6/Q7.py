#      A 
#     A C 
#    A C E
#   A C E G
#  A C E G I

n = 5
for i in range(n):
    print(' ' * (n - i - 1), end = ' ')
    for j in range(65, 65 + (2 * i + 1), 2):
        print(chr(j), end = ' ')
    print()
