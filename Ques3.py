#Ques 3 (To calculate the factorial of a number)

factorial=1
number=int(input("Enter the number :"))
for i in range(2,number+1):
   factorial=i*factorial
print("The factorial of given number is : ", factorial)