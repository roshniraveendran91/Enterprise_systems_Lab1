def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is even.")
    else:
        print(number, "is odd.")

# Example usage
num = int(input("Enter a number: "))
check_even_odd(num)
