import sys
sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    # a, b = map(int,input().split())
    num = input()
    n = len(num)-1
    a = int(num[0])
    b = int(num[1])
    if 5<=int(num[2])<=9:
        b = int(num[1])+1
        if b==10:
            b = 0
            a = int(num[0])+1
            if a == 10:
                b = 0
                a = 1
                n += 1

    print('#{} {}.{}*10^{}'.format(tc,a,b,n))
