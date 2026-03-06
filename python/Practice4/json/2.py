import json

json_data = '{"name": "Admin", "access": true}'
data = json.loads(json_data)
print(data["name"])