# List
items = ["0-speaker", "1-mic", "2-mobile", "3-laptop"]
print(items[2])
print(items[-1])
print(items[-2])
print(items[:-1])
print(items[0:3])
print(items[:3])
print(items[2:4])
print(items[1:])
items[3]="3-pc"
items.append("4-charger")
print(items)
items = ["0-speaker", "1-mic", "2-mobile", "3-laptop"]
print("1-mic" in items)
print("1-earbuds" in items)
print(len(items))
scores=[70, 80, 90, 95, 100]
for i in scores:
    print(i/2)

print([i/2 for i in scores])
