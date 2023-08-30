def rec(number, count=0):
    if len(number) == 1:
        print(number, count)
    else:
        summa = 0
        for i in number:
            summa += int(i)
        rec(str(summa), count+1)


summa = input()
rec(summa)

