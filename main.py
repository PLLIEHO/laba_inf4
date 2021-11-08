from timeit import default_timer
t0 = default_timer()

flag = False
otv = []
otvet = ''
with open("timetable.yaml", "r", encoding="utf-8") as fileYAML:
    with open("timetable.json", "w", encoding="utf-8") as fileJSON:
        for line in fileYAML:
            if ":" in line:
                if line[-2] == ":" and line[0] != "-":
                    line = line.split(':')
                    line[0] = '"' + line[0] + '"'
                    line = line[0] + ":[\n"
                elif line[0] != "-":
                    line = line.split(': ')
                    line[0] = '"' + line[0] + '"'
                    line[1] = '"' + line[1] + '"'
                    line = ' ' + line[0] + ": " + line[1]
                else:
                    line = line.split()
                    line[0] = ''
                    line[0] = ''
                    line = " ".join(line)
                    line = line.split(':')
                    line[0] = '"' + line[0] + '"'
                    line = "- " + line[0] + ": "
            line = line.split()
            if line[0] == "-":
                if flag:
                    line[0] = "  }\n},\n" + "{\n"
                if not flag:
                    line[0] = "\n{\n"
                    flag = True
            line = " ".join(line)
            otv.append(line)
        for i in range(len(otv)):
            if otv[i][0] == "{":
                otvet = otvet + "" + otv[i]
            elif otv[i][2] != "}" and otv[i-1][-1] != ":" and otv[i-1][-1] != "[" and otv[i][-1] != "[":
                otvet = otvet + ",\n" + otv[i]
            elif otv[i-1][-1] == ':':
                otvet = otvet + "\n   {\n" + otv[i]
            else:
                otvet = otvet + "\n" + otv[i]
        otvet = otvet.replace('" ', '"')
        otvet = otvet.replace(' "', '"')
        fileJSON.write("{\n")
        fileJSON.write(otvet)
        fileJSON.write("\n  }\n}")
        fileJSON.write("\n  ]\n}")
        fileJSON.close()
t1 = default_timer() - t0
print("Время выполнения теста 1: ", t1*10)


