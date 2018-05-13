import csv

flats_list = list()

with open('output.csv', newline='') as csvfile:
	flats_csv = csv.reader(csvfile, delimiter=';')
	flats_list = list(flats_csv)


# TODO 1:
# Напишите цикл, который проходит по всем квартирам, и печатает только новостройки
# и их порядковые номера в файле. Подсказка:
for i, flat in enumerate(flats_list):
  if "новостройка" in flat:
    print('{0} --> {1}'.format(i, flat))


# TODO 2:
# При помощи пересечения множеств попробуйте сравнить больше двух новостроек между собой одновременно
# например, пересечение 3 и 6 квартиры из файла с ЦИАНа делается так:
# flats_intersesction = set(flats_list[2]) & set(flats_list[5])

#  Для пересечения множеств новостроек сначала получим список порядновых номеров новостроек
new_flats_number_lst = []
for i, flat in enumerate(flats_list):
    if "новостройка" in flat:
        new_flats_number_lst += [i]  # Накапливаем порядковые номера новостроек в список
print('Список порядковых номеров новостроек:', new_flats_number_lst)


# Теперь мы можем пройтись по новостройкам с цикле и сделать их пересечение
# Получили результат пересечения множест первых двух новостроек
flats_intersesction = set(flats_list[new_flats_number_lst[0]]) & set(flats_list[new_flats_number_lst[1]])
ind = 2  # Задали начальных индекс элементов с списке new_flats_number_lst для начала цикла while
while True:
    if ind < len(new_flats_number_lst):
        flats_intersesction = flats_intersesction & set(flats_list[new_flats_number_lst[ind]])
        ind += 1
    else:
        break
print('Получили результат пересечения всех квартир:', flats_intersesction)


# TODO3:
# Вот так мы превратили наш массив квартир в словарь, где ключом является уникальный номер объявления,
# а значением - ссылка на страничку с объявлением.
# Измените код так, чтобы стало наоборот.
test_dict = dict()
for i, flat in enumerate(flats_list):
  if i == 0:
    continue
  test_dict[flat[len(flat)-1]] = flat[0]
print (test_dict)

