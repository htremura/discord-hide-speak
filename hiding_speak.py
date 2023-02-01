import pyperclip
import string

jazzystring = ""
emote = False

boring = input("Gimme text to make a difficult to read secret!\n").upper()

for letter in range(len(boring)):
    if boring[letter] == ":":
        if emote == False:
            emote = True
            jazzystring += "||" + boring[letter]
        else:
            emote = False
            jazzystring += boring[letter] + "||"
    else:
        jazzystring += "||`" + boring[letter] + "`||"

print("\n" + str(len(boring)) + " characters in the input string.\n" + str(len(jazzystring)) + " characters for it all spoilered.")  
pyperclip.copy(jazzystring)
