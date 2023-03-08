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

def decode():
    pass

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
            encode(password)
            print('Your password has been encoded and stored!')
            print()

        elif choice == 2:
            print(f'The encoded password is {new_code}, and the original password is {old_code}.')
            print()

        elif choice == 3:
            no_stop = False

if __name__ == '__main__':
    main()