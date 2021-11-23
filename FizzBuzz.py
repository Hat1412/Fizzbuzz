num = int(input("Enter number:"))
num2 = int(input("Enter number:"))

for i in range(1,20):
    if(i % num == 0 and i % num2 == 0):
        print("FizzBuzz")
    elif(i % num == 0):
        print("Fizz")
    elif(i % num2 == 0):
        print("Buzz")
    else:
        print(i)

    
