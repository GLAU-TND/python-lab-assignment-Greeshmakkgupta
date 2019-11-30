b=int(input())
c=int(input())
try:
    a=b+c
    print(a)
except TypeError:
    print('mismatch type')
