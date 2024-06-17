#                                       DOUBT
#open both files 
with open('Ques 25.txt','r') as firstfile, open('Output Ques 25.txt','a') as secondfile: 
       
    for line in firstfile: 
             secondfile.write(line)