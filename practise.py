
print("welcome to chuks cafe")
name =input("what's your name?: ")
if name == "bob" or name == "rohit":
    evel_status = input("are you evil " + name + "?:")
    if evel_status == "yes":
        print("you are not allowed to enter")
        exit()
    else:
            print("welcome to chuks cafe" + name)
else:
    print("welcome to chuks cafe " + name)
menu = "coffee,tea, black cofee,cold cofee,hot cofee,capicino,espressp"
print(" This is our menu,we have: "+ menu)
order = input("what would you like to order?:")
print(" Thank you for ordering " + order + " your order will be ready in 5 minuts")
price = 300
quentity = input ("how many " + order +" would you like to order? :")
print("your total bill is :"+ str(price*int(quentity)) + "rupees")
 