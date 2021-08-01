import sys
sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    a, b = map(int,input().split())
    if 0<a<10 and 0<b<10:
        res = a*b
    else :
        res = -1
    print('#{} {}'.format(tc,res))
