#Ване на день рождения подарили n кубиков. Он с друзьями решил построить из них пирамиду.
#Ваня хочет построить пирамиду следующим образом: на верхушке пирамиды должен находиться
#1 кубик, на втором уровне — 1 + 2 = 3 кубика, на третьем — 1 + 2 + 3 = 6 кубиков, и так далее.
#Таким образом, на i-м уровне пирамиды должно располагаться 1 + 2 + ... + (i - 1) + i кубиков.
#Ваня хочет узнать, пирамиду какой максимальной высоты он может создать с использованием имеющихся кубиков.
n=int(input())
level=0
cub_level=0
s=0
while s<n:
    level+=1
    cub_level+=level
    s+=cub_level
if s==n:
    print(level)
else:
    print(level-1)

