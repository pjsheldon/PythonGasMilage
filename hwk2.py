'''--------By: PJ Sheldon---------
	--------Date: 7/17/20---------
	hwk2.py programming assignment 2
	SEC-290 Wilmington University'''


print("Automobile Fuel Cost Calculator")

print('') # line space, I experimented this gave me my desired look.
#used \n to give line breaks
print("This program may help you decide which car makes sense for you based on \nyour budget. You will be asked to enter the MPG for the car you have in mind,\nthe average number of miles you expect to drive each month and the cost per\ngallon for fuel.")

print('')

print("The program will then calculate the monthly fuel cost.")

print('')
# x is for MPG
x = float(input("Please enter the car’s MPG (miles per gallon): ")) 

# y is for miles
y = float(input("Please enter the average number of miles driven per month: "))

# p is for gas price
p = float(input("Please enter the cost of fuel per gallon: $"))

# gallons per month equation
gallons = float(y / x)
# price per month equation 
price = float(gallons * p) 

print('')

print("Given the price of fuel at ${}/gallon and {} miles/month travled:".format(p, y)) # didnt need to add decimal place here but can if needed.

print('')

print("Gallons used each month: {:.1f}".format(gallons)) # extra credit: with adding a : made it work
print("Monthly cost of fuel: ${:.2f}".format(price)) 

print('')
print("Hope this helps!") # ending message