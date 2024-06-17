celsius = 37
fahrenheit = (celsius * 1.8) + 32
print('%.2f Celsius is equivalent to: %.2f Fahrenheit' % (celsius, fahrenheit))

temp=("Enter your choice :")
choice=input("Do you wanr to calculate temperature in Celsius or Farenheit? ")

while True:
        if choice == 'Frenheit':
                
                celsius = float(input("Enter temperature in celsius: "))
                fahrenheit = (celsius * 1.8) + 32
                print(str(celsius )+ " degree Celsius is equal to " + str(fahrenheit )+ " degree Fahrenheit.")
        else:
                fahrenheit = float(input("Enter temperature in fahrenheit: "))
                celsius = (fahrenheit - 32)/1.8
                print(str(fahrenheit )+ " degree Fahrenheit is equal to " + str(celsius ) + " degree Celsius." )
       