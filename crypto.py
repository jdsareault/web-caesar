import string

import string

def alphabet_position(letter):
    letter_lc = letter.upper()
    number = (ord(letter_lc) - 65)
    return number

def rotate_character(char, rot):
    if(char in string.ascii_uppercase):
        newPos = (alphabet_position(char) + rot) % 26
        return letter_from_pos(newPos, "upper")
    elif(char in string.ascii_lowercase):
        newPos = (alphabet_position(char) + rot) % 26
        return letter_from_pos(newPos, "lower")
    else:
        return char

def letter_from_pos(num, case):
    if(case == "upper"):
        ascii_pos = num + 65
        return chr(ascii_pos)
    elif(case == "lower"):
        ascii_pos = num + 97
        return chr(ascii_pos)
    else:
        print("""Error. Input a valid case ('upper'/'lower')""")
        
def encrypt(text, rot):
    newString = text
    for i in range(len(text)):
        newString = (newString[:i] + rotate_character(newString[i], rot)
                     + newString[i+1:])
    return newString
