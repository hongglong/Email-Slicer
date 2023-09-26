#get users email
email_input = input("Enter Your Email: ")

#split username and domain
user, domain = email_input.split("@")

#Print username and domain
print(f"username: {user}\ndomain name: {domain}")
