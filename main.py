"""
    @Smirnov_Sergei for Yandex
    Мерж двух таблиц. Добавление в таблицу visits записей о revenue
 """
import csv

with open("visits_py.txt", 'r+') as f:
    text = ''.join([line.replace(",", ".") for line in f.readlines()])
    f.seek(0)
    f.write(text)
with open("purchases_py.txt", 'r+') as f:
    text = ''.join([line.replace(",", ".") for line in f.readlines()])
    f.seek(0)
    f.write(text)


visits_data = []
purchases_data = []

with open("visits_py.txt") as f:
    for line in f:
        visits_data.append([float(x) for x in line.split()])

with open("purchases_py.txt") as f:
    for line in f:
        purchases_data.append([float(x) for x in line.split()])


f = open("result_py.txt", 'r+')
for i in range(len(visits_data)):
    for j in range(len(purchases_data)):
        if (purchases_data[j][0] == visits_data[i][0]) \
                and (visits_data[i][1] <= purchases_data[j][2] <= visits_data[i][2]):
            visits_data[i].append(purchases_data[j][1])
            visits_data[i].append(purchases_data[j][2])

    for j in range(len(visits_data[i])):
        f.write("%s " % visits_data[i][j])
    f.write("\n")


# преобразование для дайльнейшей работы в Excel
with open("result_py.txt", 'r+') as f:
    text = ''.join([line.replace(".", ",") for line in f.readlines()])
    f.seek(0)
    f.write(text)