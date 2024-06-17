#Ques 6 

file1='sample.txt'

try:
    with open("C:/Python ML/File.txt",'r') as file:
        file1=file.read()
        print("The file content is: ",file1)
except FileNotFoundError:
     print("File not found")