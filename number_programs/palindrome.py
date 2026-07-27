
def is_palindrome(number):
    original_number = number
    reverse_number = 0

    while number > 0:
        digit = number % 10
        reverse_number = reverse_number * 10 + digit
        number //= 10

    return original_number = reverse_number



input_number = int(input("Enter a number: "))


if is_palindrome(input_number):
    print(f"{input_number} is a Palindrome Number.")
else:
    print(f"{input_number} is Not a Palindrome Number.")