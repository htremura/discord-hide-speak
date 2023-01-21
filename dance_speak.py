import pyperclip
import string

letterlist = string.ascii_uppercase + "0123456789"
jazzystring = ""

boring = input("Gimme text to make dance!\n").upper()
nitro = input("Do you have NITRO? (y/n)")
if(nitro=="y" or nitro==""):
    for letter in range(len(boring)):
        if boring[letter] in letterlist:
            jazzystring += ":" + boring[letter] + "_:"
        elif boring[letter] == " ":
            jazzystring += ":__:"
        elif boring[letter] == "?":
            jazzystring += ":QSTN:"
        elif boring[letter] == "@":
            jazzystring += ":AT:"
        elif boring[letter] == "&":
            jazzystring += ":AMPRSND:"
        elif boring[letter] == "$":
            jazzystring += ":DLLR:"
        elif boring[letter] == "!":
            jazzystring += ":BANG:"
        elif boring[letter] == ".":
            jazzystring += ":DOT:"
        else:
            jazzystring += boring[letter]
    print("\n" + str(len(boring)) + " emotes copied to clipboard.\n" + str(len(jazzystring)) + " characters for those emotes.")            
else:
    for letter in range(len(boring)):
        if boring[letter] in letterlist:
            jazzystring += "\:" + boring[letter] + "\_\:"
        elif boring[letter] == " ":
            jazzystring += "\:\_\_\:"
        elif boring[letter] == "?":
            jazzystring += "\:QSTN\:"
        elif boring[letter] == "@":
            jazzystring += "\:AT\:"
        elif boring[letter] == "&":
            jazzystring += "\:AMPRSND\:"
        elif boring[letter] == "$":
            jazzystring += "\:DLLR\:"
        elif boring[letter] == "!":
            jazzystring += "\:BANG\:"
        else:
            jazzystring += boring[letter]
    print("\n" + str(len(jazzystring)) + " regular characters copied to clipboard")    
pyperclip.copy(jazzystring)
