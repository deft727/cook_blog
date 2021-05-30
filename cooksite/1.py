# from collections import defaultdict

# def group(files):
#     owners=defaultdict(list)
#     for file,owner in files.items():
#         owners[owner].append(file)
#     return owners

# files = {
#     'input.txt':'Randy',
#     'code.py':'Stan',
#     'output.py':'Randy'
# }

# print(group(files))

# for i in enumerate("hello world"):
#     print (i)


# _________________________________________________


# words = '''during - вовремя
# conversation - разговор
# accident - случайно
# junp over - перепрыгнул
# guilt - вина
# check out - выехать
# remeined  - остался
# effords - усилия 
# introduce - представлять
# a favour - одолжение
# put off - откладывть
# quikly - тихо
# loudly - громко 
# considerebly -значительно  
# significantly - значительно
# moved - переехать
# consider - считать
# opportunity - возможность
# reviced - повторил
# gave up - сдаться
# getting touch - связаться
# matter - дело 
# partly - частично
# divided - делить
# appeared - появился
# suddenly -вдруг
# immediately - сразуже
# greatly - сильно
# described - описал
# quite rary - довольно редко
# issue - вопрос
# fill in - заполнил
# annifarsary - годовщина
# tended - склоны
# deserve - заслужить 
# almost - практически
# figues - цифры
# recive- изобретать
# lend - приводить
# catch - поймать
# current - текущая
# be out - отсутствует
# require - требовать
# innocent - невинный
# detend - защащать
# enemy - враг
# the flanc - забор
# outstanding - выдающийся
# let - позволять
# leave - уезжать
# brought - принес
# mean - намереваться
# sit - сидеть
# stand - стоять
# lose - терять
# meet - встречаь
# set - ставить
# classmate - одноклассник
# set up - основать                           
# by heart - наизусть
# pieces- куски
# sell - продавать
# grow - расти
# contest - конкурс
# by - покупать
# space - пространство
# send - отправить
# notification - уведомление
# healtly - здоровье
# definite - определенное
# hurt - ушиб
# arm -рука
# properly - правильно 
# thief - вовр
# masterpeace - шедевр
# stick - палка
# elbow - локоть
# stomach - живот
# press-ups - отжимания
# sword - меч
# half - половина
# headache - головная боль
# Waiter - оффициант
# return - возвращаться
# nearly - около
# nearest - ближайший
# survey - опрос
# sights - достопремичательность
# far too -  чересчер
# pick up - поднять
# to take a holiday - отправиться в отпуск
# to carry - нести
# room - пространство
# to take an exam - сдавать экзамены
# pills - таблетки
# take pills - принимать таблетки
# a bun - булочка
# porridge - каша
# sausage - колбаса
# sausages - сосики
# potatos - картошка
# have for supper - есть на поздний ужин
# be thirsty - ипытывать жажду
# i`m thirsty - я хочу пить 
# besides - кроме того
# castle - замок 
# place - место
# charities - благотворительная организация
# visitor - посетитель
# Racehorse -каковая лошадь
# lawyer - адвокат
# insect - насекомое
# terrible - ужасный
# tears - слузы
# eyes - глаза
# shine - светиться
# to be late - опаздывать'''

# x={}
# for i in words.split('\n'):
    
#     x.setdefault(i.split('-')[0].strip(),i.split('-')[1].strip())

# name = ''  
# while name != '0':
#     name = input('Введите слово: (добавить 1,удалить 2 , изменить 3, выйти 0) ')
#     res=x.get(name.strip().lower())
#     if name == '0':
#         print('end')
#     elif name == '1':
#         add = input ('Веведите слово и перевод через пробел: ').split(' ')
#         if x.get(add[0].strip()):
#             print('Такое слово уже существует')
#             continue
#         x[add[0].strip()]=add[1].strip()
#     elif name  == '2':
#         delete = input('Введите слово для удаления ')
#         if x.get(delete):
#             try:
#                 x.pop(delete)
#                 print(f'слово {delete} было удалено')
#             except:
#                 print('чтото пошло не так')
#                 continue
#         else:
#             print(f'слово {delete} небыло найдено')
#             continue
#     elif name == '3':
#         change = input('введите слово которое хотите изменить: ')
#         if x.get(change):
#             translate = input ('Введите перевод: ')
#             x[change] = translate
#         else:
#             print(f'слово {change} не найдено')
#     else:
#         print (f'{name} = {res}')



# def add_students():
#     name = input("Введите имя: ")
#     while True:
#         try:
#             grade = int(input("Введите оценку: "))
#         except ValueError:
#             print("Вы ввели не число")
#             continue
#         else:
#             return name,grade


# def sort_students(students):
#     good_grate = "Поступили: "
#     bad_grate = "Не поступили: "
#     for name,grade in students.items():
#         if grade >= 4:
#             good_grate += f'\n{name} - {grade}'
#         elif grade <= 3:
#             bad_grate += f'\n{name} - {grade}'
#     print(good_grate)
#     print(bad_grate)


# def main():
#     students = {}

#     command=''
#     while command != '0':
#         command = input("1 - Добавить\n2 - просмотреть\n0 - Выйти \nВведите команду ")
#         if command == '1':
#             name,grade = add_students()
#             students[name] = grade
#         elif command == '2':
#             sort_students(students)

# if __name__ == '__main__':
#     main()

# def my_func(var=[]):
#     var.append('my_element1')
#     return var

# print(my_func())

import re
mystr='fssa43asda 21 asd3fasdf5fds5,32,1,qwdsd3'
# num = []
# tmp = ''
# for i in mystr:
#     if i.isdigit():
#         tmp += i
        
        
#     if not i.isdigit():
#         if tmp:
#             num.append(tmp)
#         tmp= ''
# if i.isdigit():
#     num.append(i)

# print(num)

# nums = re.findall('[0-9]+',mystr)
# print(nums)
# numbers = []
# for i in nums:
#     numbers.append(int(i))
# print(numbers)

nums = [int(i) for i in re.findall('\d+',mystr)]
print(nums)