student = {
    "name" : "laraib",
    "age" : 25,
    "gender" : "male",
    "qualified" : False
}

print(student)

print(student["age"])

student["name"] = "siddiqui"
print(student["name"])

# key values are linked using ":"

for key in student:
    print(key)

for value in student.values():
    print(value)

for k,v in student.items():
    print(k, v)

for k in student:
    if k == "name":
        print("found the key")

if "name" in student:
    print(True)
else:
    print(False)
    