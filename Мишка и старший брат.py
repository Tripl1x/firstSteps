a,b=map(int,input().split())
if a>b:
    print("Вес Боба уже больше веса Лимака")
elif a<b:
    years=0
    while a<=b:
        a=a*3
        b=b*2
        years+=1
print(years)
        
