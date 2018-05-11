import csv

flats_list = list()

with open('output.csv', newline='') as csvfile:
	flats_csv = csv.reader(csvfile, delimiter=';')
	flats_list = list(flats_csv)

#можете посмотреть содержимое файла с квартирами через print, можете - на вкладке output.csv
# print (flats_list)


#TODO 1:
#Напишите цикл, который проходит по всем квартирам, и печатает только новостройки
#и их порядковые номера в файле. Подсказка:
# for i, flat in enumerate(flats_list):
#   if "новостройка" in flat:
    # print('{0} --> {1}'.format(i, flat))


#TODO 2:
#При помощи пересечения множеств попробуйте сравнить больше двух новостроек между собой одновременно
#например, пересечение 3 и 6 квартиры из файла с ЦИАНа делается так:
# flats_intersesction = set(flats_list[2]) & set(flats_list[5])

# сравнение больше новостроек между собой
new_flats_number_lst = []
for i, flat in enumerate(flats_list):
    if "новостройка" in flat:
        new_flats_number_lst += [i]  # Накапливаем порядковые номера новостроек в список
# print('Список порядковых номеров новостроек:', new_flats_number_lst)

while len(new_flats_number_lst) > 1:
    flats_intersesction = set(flats_list[new_flats_number_lst[0]]) & set(flats_list[new_flats_number_lst[1]]) & set(flats_list[new_flats_number_lst[2]]
    print(flats_intersesction)
    # print('Результат сравнение новостроек №№ {0},{1},{2} --> {3}'.format(new_flats_number_lst[0], new_flats_number_lst[1], new_flats_number_lst[2], flats_intersesction))
    del new_flats_number_lst[2]
    del new_flats_number_lst[1]
    del new_flats_number_lst[0]

# --> Остановился на том, что не получается в цикле сделать пересечение трех и более множеств. Надо понять как контролировать окончание элементов в
# new_flats_number_lst.

# count_new_flats = len(new_flats_number_lst)
# print('count_new_flats', count_new_flats)
# ind = 0
# while count_new_flats > 1:
#     flats_intersesction = set(flats_list[ind]) & set(flats_list[ind+1]) & set(flats_list[ind+2])
#     ind += 3
#     print('Результат сравнение новостроек №№ {0},{1},{2} --> {4}'.format(i-2, i-1, i, flats_intersesction))

# flats_intersesction = set(flats_list[i-2]) & set(flats_list[i-1]) & set(flats_list[i])



#Порядковые номера новостроек вы уже получили при выполнении предыдущего задания.
#Не забудьте вывести результат функцией print

#TODO3:
#Вот так мы превратили наш массив квартир в словарь, где ключом является уникальный номер объявления,
#а значением - ссылка на страничку с объявлением.
#Измените код так, чтобы стало наоборот.
test_dict = dict()
for i, flat in enumerate(flats_list):
  if i == 0:
    continue
  test_dict[flat[0]] = flat[len(flat)-1]
# print (test_dict)

