nation = ("korea","japan","china")
print(nation)
a = input("nation")
try:
    print(nation.index(a))
except:
    print("error")
b = input("index")
try:
    print(nation[int(b)])
except:
    print("no")