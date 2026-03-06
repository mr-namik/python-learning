import json

data = {
    "name": "Ivan",
    "skills": ["Python", "Git"],
    "is_student": True,
    "projects": None
}


json_string = json.dumps(data, indent=4)
print(json_string)

# PYTHON --> JSON
#json.dumps() - Берет объект Python и превращает его в строк
#json.dump() — (Dump) Берет объект Python и записывает его в файл.

#JSON --> PYTHON
#json.loads() - обрaтно в строку Python