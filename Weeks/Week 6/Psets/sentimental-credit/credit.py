# function to check if the card number is valid using Luhn's algorithm
def is_valid(card_number):
    total = 0
    num_digits = len(card_number)
    length_parity = num_digits % 2

    for i in range(num_digits):
        digit = int(card_number[i])

        # Double every second digit from the right
        if i % 2 == length_parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        
        total += digit
    return total % 10 == 0


def get_card_type(card_number):
    if card_number.startswith("4") and len(card_number) in [13, 16]:
        return "VISA"
    elif(card_number.startswith(("34", "37"))) and len(card_number) == 15:
        return "AMEX"
    elif card_number[:2] in [str(i) for i in range(51, 56)] and len(card_number) == 16:
        return "MASTERCARD"
    else:
        return "INVALID"
    

# get input from user
card_number = input("Card Number: ")
if is_valid(card_number):
    print(get_card_type(card_number))
else:
    print("INVALID")