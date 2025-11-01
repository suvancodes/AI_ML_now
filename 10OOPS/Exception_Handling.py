class error(Exception):
    pass
class grater(error):
    pass
class less(error):
    pass
try:
    name = input('enter your name: ')
    year = int(input('enter your age: '))
    age = 2025 - year
    if age>=20 and age<=30:
        print('that is a valid age')
    elif age<20:
        raise less
    else:
        raise grater
except less:
    print('your age should be grater then 20')
except grater:
    print('your age should be less then 30')
    
    
