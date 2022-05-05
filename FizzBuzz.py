num = 3
num2 = 5
mes = ""

for i in range(101):
    mes = ""

    if(i % num == 0):
        mes += "Fizz"

    elif(i % num2 == 0):
        mes += "Buzz"

    if not mes:
        mes += str(i)

    print(mes)

    
