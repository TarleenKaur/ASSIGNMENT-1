str1 = "HELLO WORLD"
count = {}
for i in str1:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print("Count of all characters in HELLO WORLD is : " ,(count))