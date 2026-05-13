import json

data = {
    "name": "홍길동",
    "age": 25,
    "city": "서울"
}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)