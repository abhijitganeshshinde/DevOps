def prime_numbers(n):
    prime_numbers = []
    for number in range(2, n):
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(number)
    return prime_numbers

n = int(input("Enter the number :"))
list_prime_numbers = prime_numbers(n)
print("Prime numbers up to", n, ":")
for prime in list_prime_numbers:
    print(prime)
