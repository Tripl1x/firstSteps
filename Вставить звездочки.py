def zvezd(a):
    if len(a)==1:
        return a
    if len(a)==2:
        return a[0]+"*"+a[1]
    if len(a)>2 and len(a)<=1000:
        return a[0]+"*"+zvezd(a[1:-1])+"*"+a[-1]
a=input()
print(zvezd(a))
    