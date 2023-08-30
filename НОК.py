A,B=map(int,input().split())
y=A*B
while B>0:
      A,B=B,A%B
print("НОК чисел равняется",y/A)
