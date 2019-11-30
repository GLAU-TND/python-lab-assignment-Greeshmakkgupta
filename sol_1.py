class MyException(Exception):
    def __init__(self, v,s):
        self.v = v
        self.s=s
try:
    v=int(input())
    s=int(input())
    print(v+s)
except MyException as error:
    print('Custom exception occured')