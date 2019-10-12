# def great(name ='buddy',time='all'):
#     print(f'Good {time} {name}, hope you are well')
# name = input('enter your name:')
# time = input('Enter the time of day:')
# if name == '' or time == '':
#     great()
# else:
#     great(name,time)
def area(radius):
    print(3.142*radius*radius)
    return 3.142*radius*radius
def val(area, length):
    print(area*length)
radius = int(input('Enetr a radius:'))
length = int(input('Enter the length:'))
val( area(radius), length)
