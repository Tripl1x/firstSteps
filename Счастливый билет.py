ticket_number=int(input())
a=ticket_number//100000
b=ticket_number//10000%10
c=ticket_number//1000%10
d=ticket_number//100%10
e=ticket_number//10%10
f=ticket_number%10
if a+b+c==d+e+f:
    print("У вас счастливый билет")
else:
    print("Увы")
