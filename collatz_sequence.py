def collatz(n):
    if n == 2:
        return n // 2
        a = n // 2
        print(int(a))
    elif n == 1:
        return 3 * (n + 1)
        b = 3 * (n + 1)
        print(int(b))
    else: 
        return 0
        print('number is neither even nor odd')

n = int(input())
collatz(n)

\
