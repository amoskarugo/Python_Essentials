

def is_a_palidrome(string):
    my_string = (string.replace(" ", "")).lower()
    if my_string == " " or my_string == "":
        return False
    div = (len(my_string)) // 2
    for i in range(div):
        if my_string[i] != my_string[-1 + -i]:
            return False
    return True

text = input("Enter text to che whether its a palidrome: ")
if is_a_palidrome(text):
    print("It's a palindrome")
else:
    print("It's not a palindrome")