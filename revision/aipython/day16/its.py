myTuple=(1,2,3)
print(myTuple)

print(myTuple[2])

tp1=(1,2,3)
tp2=("a","b","c")

print(tp1+tp2)

tp3=(1,)
print(tp3*10)

a, b, c = (10,20,20)
print(b)

#set
ls=[1,2,3,3]
print(set(ls))

s1={1,2,3}
s2={2,3,4}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))