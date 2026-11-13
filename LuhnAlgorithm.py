def verify_card_number(card_num):
    stripped_num = card_num.replace(" ", "").replace("-", "")
    
    digits = [int(d) for d in stripped_num]

    sum = 0
    even_digit = len(digits) % 2 == 0
    odd_digit = len(digits) % 2 != 0
    check_digit = len(digits) - 1
    i = len(digits) - 1
    while i >= 0:
        if even_digit:
            if i % 2 == 0:
                doubled_value = digits[i] * 2
                if doubled_value > 9:
                    doubled_value -= 9
                    sum += doubled_value
                else:
                    sum += doubled_value
            else:
                sum += digits[i]
        elif odd_digit:
            if i % 2 != 0:
                doubled_value = digits[i] * 2
                if doubled_value > 9:
                    doubled_value -= 9
                    sum += doubled_value
                else:
                    sum += doubled_value
            else:
                sum += digits[i]
        i -= 1
    if sum % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'



print(verify_card_number('453914889'))
print(verify_card_number('4111-1111-1111-1111'))
print(verify_card_number('1234 5678 9012 3456'))
print(verify_card_number('453914881'))
