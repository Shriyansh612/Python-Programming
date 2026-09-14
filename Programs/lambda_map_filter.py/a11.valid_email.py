emails = ["hellogmail.com","Hrllo.com","Hello@gmail.com","Hello@yahoo.com"]

valid_emails = list(filter(lambda email:'@'in email,emails))
print(valid_emails)

print(list(map(lambda email:email.lower(),valid_emails)))