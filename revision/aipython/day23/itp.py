import pandas as pd

d = {'People':['P1','P2', 'P3'], 'Age':[20,30,40]}
print(d)

df=pd.DataFrame(d)
print(df)
print(df["People"])
print(df["Age"].mean())
print(df["Age"].sum())
print(df["Age"].std())
print(df[df["Age"] >= 30]["People"])


# pd.read_excel("score_updated.xlsx")
# pd.read_csv("score.csv")

print(df.to_csv("sample.csv", index=False))
rc=pd.read_csv("sample.csv")
print(rc)

