import sys
sys.stdin = open('input.txt', 'r')
A, B = map(int, input().split())

if A == 2 and B == 1:
    print('A')
elif A == 2 and B == 3:
    print('B')
elif A == 1 and B == 2:
    print('B')
elif A == 1 and B == 3:
    print('A')
elif A ==3 and B == 1:
    print('B')
elif A == 3 and B == 2:
    print('A')