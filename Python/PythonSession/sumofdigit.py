inputvalue = int(input("Enter The Value :"))

def sum_of_digit(number):
    sum =0
    while number > 0:
        rem = number % 10
        sum += rem
        number = number // 10
    return sum

sum_of_digit_Value = sum_of_digit(inputvalue)

print(sum_of_digit_Value)