X1,Y1=map(int,input().split())
X2,Y2=map(int,input().split())
a=abs(X1-X2)
b=abs(Y1-Y2)
if a==b and 1<=X2<=8 and 1<=Y2<=8:#Условие возможности перемещения слона только по диагонали,
                                  #а также его попадение в клетку шахматной доски
    print('Yes')
else:
    print('NO')
