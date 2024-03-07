##Author: Eve Droge
##This code is meant to mimick the following example output text as well as allow similar depicted user interaction
##***************************************
##My Coffee and Muffin Shop
##Number of coffees bought?
##1
##Number of muffins bought?
##2
##***************************************
##
##***************************************
##My Coffee and Muffin Shop Receipt
##1 Coffee at $5 each: $ 5.00
##2 Muffins at $4 each: $ 8.00
##6% tax: $ .78
##---------
##Total: $ 13.78
##***************************************
#and adding new additions to this menu

#I like making really annoying to read print statements to print blocks of statements
print("***************************************\nMy Coffee and Muffin Shop\nNumber of coffees bought?\n")
#Both of these create variables for the numbers of coffees and muffins respectively that the user wants
coffees = input()
muffins = input("\nNumber of muffins bought?\n")
cakePop = input("\nNumber of cake pops bought?\n")
waters = input("\nNumber of bottled waters bought?\n")
#Trial and error has reminded me that C and Python don't treat variables similar
#therefore I accidentally made the following block of strings repeat the number of coffees 5 times instead of printing that value times five.
#coding is a funny thing sometimes
#The next lines convert the inputs to integers, and find values for their prices
coffees = int(coffees)
muffins = int(muffins)
cakePop = int(cakePop)
waters = int(waters)
cakePopPrice = 2*cakePop
watersPrice = waters
coffeePrice = coffees * 5
muffinsPrice = muffins * 4
print("***************************************\n\n***************************************\nMy Coffee and Muffin Shop Receipt\n" + str(coffees) + " Coffee @ $5 each: $ " + str(coffeePrice) + ".00\n" + str(muffins) + " Muffins @ $4 each: $ " + str(muffinsPrice) + ".00\n")
print(str(cakePop) + "Cake pops @ $2 each: $ " + str(cakePopPrice) + ".00\n")
print(str(waters) + "waters @ 1$ each: $ " + str(waters) + ".00\n")
tax = 0.06 * (muffinsPrice+coffeePrice+waters+cakePopPrice) #determines the sales tax on coffee
print("6% tax: $" + str(tax)) #ngl, I get nervous when projects like this say anything about appropriate documentation because I never know if teachers want me to like comment ever print statement or just the calculations going on
print("\n---------\nTotal: $ " + str(tax+muffinsPrice+coffeePrice+cakePopPrice+waters))
print("\n***************************************")
