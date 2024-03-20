# Nancy Tadrous Lab 6 Group 15 encode function


def password_encoder(password):
    encoded_password = ''
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password


# def password_decoder


def main():
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')

        option = input('Please enter an option: ')

        if option == '1':
            password = input('Please enter your password to encode: ')
            encoded_password = password_encoder(password)
            print('Your password has been encoded and stored!')
            print('Encoded password:', encoded_password)
        elif option == '2':
            encoded_password = input('Please enter the encoded password: ')
            # decoded_password
            pass
        elif option == '3':
            print('Exiting program.')
            break
        else:
            break
