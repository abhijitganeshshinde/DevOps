inputvalue = int(input("Enter The Value :"))

def reverse_num(number):
    reverse_num =0
    while number > 0:
        rem = number % 10
        reverse_num = (reverse_num * 10) + rem
        number = number // 10
    return reverse_num

reverse_num_value = reverse_num(inputvalue)

print(reverse_num_value)