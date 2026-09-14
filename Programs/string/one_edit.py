text1 = input("Enter a string: ")
text2 = input("Enter a string: ")
text1 = text1.strip()
text2 = text2.strip()
if (text1==text2):
    print("Strings are same")
elif (len(text1)==len(text2)):
    edit = 0
    for i in range (0,len(text1)):
        if (text1[i]!=text2[i]):
            edit+=1
    if (edit==1):
        print("Strings are exactly one edit away")
    else:
        print("Strings are not one edit away")
elif(abs(len(text1)-len(text2))==1):
    if (len(text1)>len(text2)):
        temp = ""
        count=0
        for i in range (0,len(text1)):
            for j in range (0,len(text1)):
                 if (j!=i):
                     temp = temp + text1[j]
            if (temp==text2):
                count+=1
            temp="" 
        if (count==0):
            print("Strings are not one edit away")
        else:
            print("Strings are exactly one edit away")
    if (len(text2)>len(text1)):
        temp = ""
        count=0
        for i in range (0,len(text2)):
            for j in range (0,len(text2)):
                 if (j!=i):
                     temp = temp + text2[j]
            if (temp==text1):
                count+=1
            temp="" 
        if (count==0):
            print("Strings are not one edit away")
        else:
            print("Strings are exactly one edit away")            