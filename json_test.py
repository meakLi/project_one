import json
with open("test.json","r") as f:
    w = f.read()
    print(json.loads(w))
    print(type(w))

a = {
  "sex": "man",
  "marry": False,
  "num": 123,
  "lis": [1,2,3,5,8]
}
print(json.dumps(a))
print(type(a))
