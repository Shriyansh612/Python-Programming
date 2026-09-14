main = open("programs//file_handling//data.txt","r")
data = main.read()
main.close()

to_replace = input("Enter word to be replaced: ")
replace_with = input("Enter word to replace with: ")

new_data = data.replace(to_replace,replace_with)

copy = open("copy.txt","w")
copy.write(new_data)
copy.close()