def rec_mirror(stroka):
    if len(stroka)==1:
        if stroka=='(':
            return "()"
        else:
            return 2*stroka
    else:
        if (stroka[0]=='('):
            return "("+rec_mirror(stroka[1:])+")"
        else:
            return stroka[0]+rec_mirror(stroka[1:])+stroka[0]

stroka=input()
print(rec_mirror(stroka))