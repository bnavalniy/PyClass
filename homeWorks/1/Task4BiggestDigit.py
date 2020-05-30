input_digit = int(input("Введите целое положительное число: "))
rest = True
biggest = 0
while rest:
    # Cut last digit from the end
    last_digit = int(((input_digit / 10) - int(input_digit / 10)) * 10)
    # Get before last
    rest = int(input_digit / 10)
    before_last = round(((rest / 10) - (rest // 10)) * 10)
    if last_digit > before_last:
        if last_digit > biggest:
            biggest = last_digit
    input_digit = rest
print(f"The biggest digit is: {biggest}")
