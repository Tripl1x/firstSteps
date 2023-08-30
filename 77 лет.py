Name=input('Введите свое имя: ')
Age=int(input('Введите свой возраст: '))
import datetime
now=datetime.datetime.today()
year=now.year+(77-Age)
print('%s, вам исполнится 77 лет в %s'%(Name,year))
