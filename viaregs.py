import re
from timeit import default_timer
t0 = default_timer()

flag = False
otv = []
otvet = ''
i = 1
with open("timetable.yaml", "r", encoding="utf-8") as fileYAML:
    with open("timetableRegularsOld.json", "w", encoding="utf-8") as fileJSON:
        line = fileYAML.read()
        line = re.sub("\n", ',\n', line)
        line = re.sub(":,\n", ':\n', line)
        line = re.sub("- п", '{\nп', line)
        line = re.sub("- в", '{\nв', line)
        line = line + "}\n]\n}"
        line = re.sub(",\n{\nв", '\n},\n{\nв', line)
        line = re.sub(",\n}", '\n}', line)
        line = re.sub(": ", '": "', line)
        line = re.sub(",\n", '",\n', line)
        line = re.sub("\n}", '"\n}', line)
        line = re.sub('}"', '}', line)
        line = re.sub("\s{20,44}", ' ', line)
        line = re.sub('}\n]"', '"\n}\n}\n]', line)
        line = re.sub('},', '}\n},', line)

        fileJSON.write(line)
        fileJSON.close()

with open("timetableRegularsOld.json", "r", encoding="utf-8") as file:
    with open("timetableRegulars.json", "w", encoding="utf-8") as fileJSON1:
        fileJSON1.write("{\n")
        for line in file:
            if ": " in line:
                if line[0] == " " and line[1] != " ":
                    line = re.sub("^\s", '"', line)
                else:
                    line = re.sub("^\s\s", ' "', line)
            line = re.sub("г:", 'г":\n[', line)
            line = re.sub("^Ч", '"Ч', line)
            line = re.sub("^п", '"п', line)
            line = re.sub("^в", '"в', line)
            line = re.sub("ара:", 'ара":\n{', line)
            fileJSON1.write(line)

fileJSON1.close()


t1 = default_timer() - t0
print("Время выполнения теста 3: ", t1*10)


