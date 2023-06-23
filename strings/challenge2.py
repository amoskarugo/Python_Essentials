
# A LED DISPLAY
#program which is able to simulate the work of a seven-display device
#Each digit is constructed from 13 LEDs (some lit, some dark, of course) 
# (#) - LIT (whitespace) - dark

"""
sample output of 123 on the LED display
  #  ####  #### 
  #     #     # 
  #  ####   ### 
  #  #        # 
  #  ####  #### 

"""


zero = "{}\n{}\n{}\n{}\n{}\n".format("#"* 3, "# #", "# #", "# #", "#" * 3)
one =  "{}\n{}\n{}\n{}\n{}\n".format("#", "#", "#", "#", "#")
two = "{}\n{}\n{}\n{}\n{}\n".format("#"* 3, "  #", "#"* 3, "#  ", "#" * 3)
three = "{}\n{}\n{}\n{}\n{}\n".format("#"* 3, "  #", "#"* 3, "  #", "#" * 3)
four = "{}\n{}\n{}\n{}\n{}\n".format("# #", "# #", "#"* 3, "  #", "  #")
five = "{}\n{}\n{}\n{}\n{}\n".format("#"* 3, "#  ", "#"* 3, "  #", "#" * 3)
six = "{}\n{}\n{}\n{}\n{}\n".format("#" * 3, "#  ", "#"* 3, "# #", "#" * 3)
seven = "{}\n{}\n{}\n{}\n{}\n".format("#"* 3, "  #", "  #", "  #", "  #")
eight = "{}\n{}\n{}\n{}\n{}\n".format("#"* 3, "# #", "#"* 3, "# #", "#" * 3)
nine = "{}\n{}\n{}\n{}\n{}\n".format("#"* 3, "# #", "#"* 3, "  #", "#" * 3)
negativ_sign = "{}\n{}\n{}\n{}\n{}".format(" "* 3, " " * 3, "#"* 3, " " * 3, " " * 3)
LED = [zero, one, two, three, four, five, six, seven, eight, nine]



while True:
    try:
        num = input("Enter a number to display on the LED: ")
        if num == " ":
            print("You entered nothing")
            continue
        for n in num:
            print(LED[int(n)], end="")
        print()
        break
    except ValueError:
        print("Please enter a number only")
        continue



