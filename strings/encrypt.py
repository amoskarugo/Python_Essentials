"""
The original Caesar cipher shifts each character by one:
a becomes b, z becomes a, and so on. Make it a bit harder, 
and allow the shifted value to come from the range 1..25 inclusive.
"""
"""
let the code preserve the letters' case (lower-case letters
 will remain lower-case) and all non-alphabetical characters
 should remain untouched
"""
#The Caesar Cipher: encrypting a message
#asks the user for one line of text to encrypt
#asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
#prints out the encoded text.

while True:
    try:
        text = input("Enter the message to encrypt: ")
        if text == "" or text == " ":
            print("text cannot be empty")
            continue
        shift = int(input("Enter shift value(1 - 25): "))
        if shift < 1 or shift > 25:
            print("shift value should be in the range(1 - 25)")
            continue
        cipher = ""
        if text.isalpha():
            for char in text:
                if char.isdigit() or char.isspace():
                    cipher += char
                    continue
                code = ord(char) + shift
                if ord(char) <= ord('z'):
                    if code > ord('z'):
                        code -= 26
                if ord(char) <= ord('Z'):
                    if code > ord('Z'):
                        code -= 26
                cipher += chr(code)
            print(cipher)
        else:
            print("enter a text with alphabetical and numerical characters only!")
            continue
        break
    except (ValueError, TypeError):
        print("an error occurred")

#The Caesar Cipher: decrypting a message
# cipher = input('Enter your cryptogram: ')
# text = ''
# for char in cipher:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char) - 1
#     if code < ord('A'):
#         code = ord('Z')
#     text += chr(code).lower()

# print(text)