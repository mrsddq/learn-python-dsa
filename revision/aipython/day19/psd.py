ls=[1,2,2,3,2,3,4,5]
print(len(ls))

numCounter={}
for i in ls:
    if i in numCounter:
        numCounter[i] += 1
    else:
        numCounter[i] = 1

print(numCounter)

temp=0
finalResult=None
for k,v in numCounter.items():
    print(f"k: {k}, v: {v}, temp: {temp}")
    if v > temp:
        temp=v
        finalResult=k
print(finalResult)