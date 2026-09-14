# text = "  My name is Shriyansh   "
# num_of_white_space = text.count(" ") - len(text.split())+1
# print(num_of_white_space)
# stripped_text = text.strip()
# print("is my data clean ?",len(stripped_text)==len(text)-num_of_white_space)\


#    "968-maria, (D@t@ Engineer );; 27y "

#   (name: maria | role: data engineer | age: 27)

text = "968-maria, (D@t@ Engineer );; 27y "
text = text.strip()
output = "("+text.replace("968-","name: ").replace(","," |").replace("(","role: ").replace("@","a").replace(");;","| age: ").replace("y","")+")"
output = output.lower()
print(output)