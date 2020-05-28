input_digit = int(input("Введите целое положительное число: "))
rest = True
biggest = 0
while rest:
    # Cut last digit from the end assume that it is biggest digit
    cutted_last = int(((input_digit / 10) - int(input_digit / 10)) * 10)
    # Get rest digits from all input
    rest = int(input_digit / 10)
    # Get last digit from the rest for comparing
    cut_from_rest = round(((rest / 10) - (rest // 10)) * 10)
    # Compare
    if biggest < cut_from_rest:
        biggest = cut_from_rest
    # continue working with rest of the digits
    input_digit = rest
print(f"The biggest digit is: {biggest}")
