dict1 = {"maths":95,
        "english":90,
        "physics":88,
        "computer":92}

dict2 = {"maths":95,
        "physics":88,
        "english":90,
        "computer":92}
c = 0
if(len(dict1)==len(dict2)):
    for key in dict1:
        if(key in dict2):
            if(dict1[key]==dict2[key]):
                continue
            else:
                c = 1
                break
        else:
            c=1
            break
    if(c==1):
        print("Dictionaries do not match")
    else:
        print("Dictionaries match")
else:
    print("Dictionaries do not match")            
        

    
