file1 = 'sample.csv'
try:
    with open(file1, 'r') as file1:
         file1_content = file1.read()
         print("File content:\n", file1_content)

except FileNotFoundError:
        print("File '{file1}' not found.")         
except Exception as i:   
        print("An error occured")   