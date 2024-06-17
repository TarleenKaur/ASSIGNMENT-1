#Ques 5 (takes a string input and write it into text file)

s_file=open('C:/Python ML/File.txt','w')
str1=input("Enter the string: ")
print("The string is:",str1,file=s_file)