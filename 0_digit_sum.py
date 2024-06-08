def find_digit_sum(number):
    if number < 10:
        return number

    remainder = number % 10 
    otherDigitsSum = find_digit_sum(number // 10)
    return remainder + otherDigitsSum



number = 238532
print(find_digit_sum(number))
