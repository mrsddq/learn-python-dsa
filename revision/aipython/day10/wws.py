# creating strings
# ================
# single_quote = 'Hello'
# double_quote = "Hello"
# triple_quote = '''Hello1
# Hello2
# Hello3
# Hello4'''
# print(single_quote)
# print(double_quote)
# print(triple_quote)

# print(single_quote[1])
# print(single_quote[-1])
# print(single_quote[:3])
# print(single_quote[:4])
# print(triple_quote[:10])

# print("Hello"+"World"+"!")
# print("Hello" + " " + "World")

# print("hahahaha "*3)

# print(len(triple_quote))

# x = "Hello World"
# print(" " in x)

# firstName = "Laraib"
# lastName = "Siddiqui"

# print(firstName.lower())
# print(lastName.capitalize())
# print(lastName.upper())

firstName = "Laraib"
lastName = "Siddiqui"

joinName = " ".join(lastName)
print(joinName)

text = "   This is a string with extra spaces. ! "
stripText = text.strip()
print(stripText)

sentence = "This is a sentence."
words = sentence.split(" ")
print(words)

text = "Hello world, hello world!"
newText = text.replace("hello", "hi")
print(newText)