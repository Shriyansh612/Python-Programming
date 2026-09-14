tup1 = tuple(map(str,input().split()))
tup2 = tuple(map(str,input().split()))

new_tup1 = ()
new_tup2 = ()
if(len(tup1)==len(tup2)):
    for i in range(256):
        if(chr(i) in tup1):
            new_tup1+=(chr(i),)*tup1.count(chr(i))
        if(chr(i) in tup2):
            new_tup2+=(chr(i),)*tup2.count(chr(i))
    if(new_tup1==new_tup2):
        print("They are anagrams")
    else:
        print("They are not anagrams")
else:
    print("They are not anagrams")                            