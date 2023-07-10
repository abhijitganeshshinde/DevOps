def prime_number(n):
    prime_numbers =[]
    for number in range(2,n+1):
        is_prime = True
        for i in range(2,number):
            if number % i == 0:
                is_prime = False
                break
            if is_prime:
                prime_numbers.append(number)
    return prime_numbers

n =20
list_of_prime_number =prime_number(n)
print("Prime numbers up to", n, ":")
for prime in list_of_prime_number:
    print(prime)