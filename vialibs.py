import yaml
import json
from timeit import default_timer
t0 = default_timer()


with open("timetable.yaml", "r", encoding="utf-8") as yaml_in:
    with open("timetableLibsOld.json", "w", encoding="utf-8") as json_out:
        yaml_object = yaml.safe_load(yaml_in)
        json.dump(yaml_object, json_out, ensure_ascii=False)
        yaml_in.close()
        json_out.close()

file_in = open("timetableLibsOld.json", "r", encoding="utf-8")
file_out = open("timetableLibs.json", "w", encoding="utf-8")
s = file_in.read()
s = s.split()
for i in range(len(s)):
    if s[i] == "null,":
        s[i] = "{"
    s[i] = s[i].replace("},", "}},")
s = " ".join(s)
file_out.write(s)
file_out.close()
file_in.close()
t1 = default_timer() - t0
print("Время выполнения теста 2: ", t1*10)
