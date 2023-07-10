def factorial(number):
    factorialnum =1
    for i in range(1,number+1):
        factorialnum *= i
    return factorialnum

inputNum = int(input("Enter The Number :"))
result = factorial(inputNum)
print(f"Factorical Number : {result}")