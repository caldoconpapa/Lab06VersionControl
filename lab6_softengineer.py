# Lab 6: Software Engineering

old_code = ''
new_code = ''
def encode(password):
    # Jonathan Vargas
    # the two global commands are to store the initial passcode
    # and encoded passcode to call later in 2. decode option
    global new_code
    global old_code
    old_code = password # store old passcode in global variable {old_code}
    p_code = list(password) # create a list from input passcode string
    e_list = [int(x) for x in p_code] # from str to int elements into a new list
    p_list = [] # create empty list to append converted numbers (new passcode list)
    for num in e_list: # for num in old list

        if 0 <= num <= 6:
            # if num is 0-6, just add 3 and add to p_list
            num1 = num + 3
            p_list.append(num1)
        elif 7 <= num <=9:
            # if num is 7-9, convert them into new numbers
            # from 7 -> 0, 8 -> 1, 9 -> 2 then append to new list
            if num == 7:
                num1 = 0
                p_list.append(num1)
            elif num == 8:
                num1 = 1
                p_list.append(num1)
            elif num == 9:
                num1 = 2
                p_list.append(num1)

    string_list = [str(x) for x in p_list]
    # convert the int elements into new list to str elements
    new_code = ''.join(string_list)
    # join the str elements in the list into a single string to be called upon in Option: 2
    return new_code

def decode(password):  # this function decodes the encoded password by subtracting 3 from each value in the numeric password

    #Julius Inocencio
    decoded = ''
    for i in password:
        x = int(i) - 3 #subtracts 3 from the current value as it loops through

        if x < 0: # if the value is less than 0, checks if there is a remainder and adds 1
            y = x % 9 #  not sure why this works, but it should be 9 % x
            decoded += str(y+1)  #adds 1 to the 'decoded' string if x < 0
        else:
            decoded += str(x)  # adds to the 'decoded' list after doing the math
    return decoded


def main():
    global new_code
    global old_code
    no_stop = True
    while no_stop:
        print('Menu')
        print('-'*13)
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        choice = int(input('Please enter an option: '))
        if choice == 1:
            password = str(input('Please enter your password to encode: '))
            encoded = encode(password) # Added encoded variable to refer to in print statement for choice 2 - Julius
            print('Your password has been encoded and stored!')
            print()

        elif choice == 2:
            decoded = decode(encode(password)) #  Added decoded variable for clarification and use in print statement - Julius
            print(f'The encoded password is {encoded}, and the original password is {decoded}.')
            print()

        elif choice == 3:
            no_stop = False

if __name__ == '__main__':
    main()