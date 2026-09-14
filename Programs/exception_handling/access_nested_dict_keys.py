dict = {1:{"name":"Shriyansh","age":19},2:{"name":"raghu","age":17}}
while True:
    try:
        person_no = int(input("Enter person number: "))
        if (person_no>2):
            raise
        key = input("Enter name or age to check the person's name or age: ")
        print(dict[person_no][key])
        break
    except Exception as err:
        print("Please enter valid key")  