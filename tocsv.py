from timeit import default_timer
t0 = default_timer()

i = 0
first = []
second = []
flagP = True
count = 1
string = "день;пара;адрес;группа;предмет;преподаватель;режим занятия;\n"
with open("timetable.yaml", "r", encoding="utf-8") as file_in:
    for line in file_in:
        line = line.replace("\n", "")
        if i == 0:
            day = line.replace(":", "")
            first.append(day)
            second.append(day)
            i += 1
        elif "пара:" in line:
            line = line.split()
            pair = line[1]
            if flagP:
                first.append(pair)
                flagP = False
            else:
                second.append(pair)
        else:
            line = line.split(": ")
            inf = line[1]
            if count < 6:
                first.append(inf)
                count += 1
            else:
                second.append(inf)
with open("timetable.csv", "w", encoding="utf-8") as file_out:
    file_out.write(string)
    first = ";".join(first)
    second = ";".join(second)
    first += ";\n"
    second += ";"
    file_out.write(first)
    file_out.write(second)
file_out.close()
t1 = default_timer() - t0
print("Время выполнения теста CSV: ", t1*10)
