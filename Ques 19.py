str1 = "Hello!! Welcome @to this place./. ;"
print("The original string is : " ,str1)
 
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for i in str1:
    if i in punc:
        str1 = str1.replace(i, "")
print("The string after punctuation filter : ", str1)