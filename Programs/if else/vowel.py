alphabet = input("Enter an alphabet: ")
if len(alphabet) !=1:
    print("Please enter only one alphabet")
elif ( alphabet.isdigit()):
    print("Please enter alphabet")
elif ( not alphabet.isdigit() and not alphabet.lower() in 'abcdefghijklmnopqrstuvwxyz'):
    print("Please enter alphabet")
# elif (alphabet=="a" or alphabet=="e" or alphabet=="i" or alphabet=="o" or alphabet=="u" or 
#     alphabet=="A" or alphabet=="E" or alphabet=="I" or alphabet=="O" or alphabet=="U"):
elif alphabet.lower() in 'aeiou':
    print("It is a vowel")
else :
    print("It is a consonant") 



# lengh function


# city = "agra"
# print(len(city))

#  if alphabet.isdigit():
#  print("number is not allowed")