thisdict = {
    'brand': "Ford",
    "model": "Mustang",
    "year": 1964
}

x = thisdict["model"]
y = thisdict.get("model")

print(x)
print(y)
print(thisdict.keys())
print(thisdict.values())

thisdict.update({'color':'red'})
print(thisdict.values())
