def main():
    print("Welcome to the Email slicer")
    print("")

    email_input = input("input your email address:")
    
    (username,domain)= email_input.split("@")
    (domain, extension)= domain.split(".")

    print("Username :", username)
    print("domain :",domain)
    print("Extension :", extension)

while True:
    main()    