num = list(map(int,input().split()))

if(num[0]>num[1] and num[0]>num[2]):
    if(num[1]>num[2]):
        lar = num[0]
        sec_lar = num[1]
        third_lar = num[2]
    else:
        lar = num[0]
        sec_lar = num[2]
        third_lar = num[1]

elif(num[1]>num[0] and num[1]>num[2]):
    if(num[0]>num[2]):
        lar = num[1]
        sec_lar = num[0]
        third_lar = num[2]
    else:
        lar = num[1]
        sec_lar = num[2]
        third_lar = num[0] 

elif(num[2]>num[0] and num[2]>num[1]):
    if(num[0]>num[1]):
        lar = num[2]
        sec_lar = num[0]
        third_lar = num[1]
    else:
        lar = num[2]
        sec_lar = num[1]
        third_lar = num[0] 

for i in range(3,len(num)):
    if(num[i]>lar):
        third_lar=sec_lar
        sec_lar=lar
        lar=num[i]
    elif(num[i]>sec_lar):
        third_lar=sec_lar
        sec_lar=num[i]    

print("Largest:",lar)        
print("Second Largest:",sec_lar)        
print("Third Largest:",third_lar)        
                      
