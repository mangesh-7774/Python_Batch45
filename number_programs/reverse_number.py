def reverse_number(number):
    reversed_num = 0

    is_negative = number < 0
    number = abs(number)
    
    while number > 0:
        last_digit = number % 10
        reversed_num = (reversed_num * 10) + last_digit
        number = number // 10
        
    return -reversed_num if is_negative else reversed_num

if __name__ == "__main__":
    user_input = int(input("Enter a number: "))
    result = reverse_number(user_input)
    print(result)