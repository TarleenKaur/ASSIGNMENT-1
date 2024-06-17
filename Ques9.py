str1=("Hello","Hi",1,2,True,False,"5+2j","Bye")
print("The given string is: ",str1)

for value in (str1):
    value= input("The value to be found is: ")
    if value in str1:
        print("The value is present in the string.")
    else:
        print("Value not found!!")