tup = tuple(map(int,input().split()))

if(tup[0]>tup[1] and tup[0]>tup[2]):
    if(tup[1]>tup[2]):
        lar = tup[0]
        sec_lar = tup[1]
        third_lar = tup[2]
    else:
        lar = tup[0]
        sec_lar = tup[2]
        third_lar = tup[1]

elif(tup[1]>tup[0] and tup[1]>tup[2]):
    if(tup[0]>tup[2]):
        lar = tup[1]
        sec_lar = tup[0]
        third_lar = tup[2]
    else:
        lar = tup[1]
        sec_lar = tup[2]
        third_lar = tup[0] 

elif(tup[2]>tup[0] and tup[2]>tup[1]):
    if(tup[0]>tup[1]):
        lar = tup[2]
        sec_lar = tup[0]
        third_lar = tup[1]
    else:
        lar = tup[2]
        sec_lar = tup[1]
        third_lar = tup[0]

sm = third_lar
sec_sm = sec_lar
third_sm = lar

for i in range(3,len(tup)):
    if(tup[i]>lar):
        third_lar = sec_lar
        sec_lar = lar
        lar = tup[i]
    elif(tup[i]>sec_lar):
        third_lar = sec_lar
        sec_lar = tup[i]

    if (tup[i]<sm):
        third_sm = sec_sm
        sec_sm = sm
        sm =tup[i]
    elif(tup[i]<sec_sm):
        third_sm = sec_sm
        sec_sm = tup[i]            

print("Largest:",lar)
print("Second Largest:",sec_lar)            
print("Third Largest:",third_lar)
print("Smallest:",sm)
print("Second Smallest:",sec_sm)
print("Third Smallest:",third_sm)
