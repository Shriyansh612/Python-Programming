text1 = input("Enter a string: ")
text2 = input("Enter a string: ")
text1=text1.strip()
text2=text2.strip()
if (len(text1)!=len(text2)):
    print("Please enter words of equal lengths")
else:
    num_of_swaps=0
    for i in range (len(text1)):
        if (text1[i]==text2[i]):
            num_of_swaps=num_of_swaps
        else:
            num_of_swaps+=1
print("Minimum number of swaps required are",num_of_swaps)                