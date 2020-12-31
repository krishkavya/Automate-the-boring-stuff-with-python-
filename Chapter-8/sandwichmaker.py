import pyinputplus as pyip
wheatp=2
whitep=2
sourdoughp=1
print("Bread :")
bread = pyip.inputMenu(['wheat','white','sourdough'])
if bread == 'wheat':
    bprice=wheatp
elif bread == 'white':
    bprice =whitep
elif bread=='sourdough':
    bprice = sourdoughp

chickenp=5
turkeyp=4
hamp=2
tofup=6
print("protein :")
protein = pyip.inputMenu(['chicken', 'turkey', 'ham','tofu'])
if protein  == 'chicken':
    pprice = chickenp
elif protein  == 'turkey':
    pprice = turkeyp
elif protein == 'ham':
    pprice = hamp
elif protein == 'tofu':
    pprice = tofup

cheddarP = 3
swissP = 1
mozzarellaP = 5
noCheeseP = 0
print("Cheese(yes/No) :")
response = pyip.inputYesNo()
if response == "yes":
    cheese = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'])
else:
    cheese = "No"
if cheese == 'cheddar':
    cPrice = cheddarP
elif cheese == 'swiss':
    cPrice = swissP
elif cheese == 'mozzarella':
    cPrice = mozzarellaP
elif cheese == 'No':
    cPrice = noCheeseP


print("mayo, mustard, lettuce, or tomato?(yes/no)")
response = pyip.inputYesNo()
if response == "yes":
   price=20
else :
  price=0

 

print("number of sandwiches required :")
number = pyip.inputInt(min = 1)
sandwichP = bprice + pprice + cPrice +price
total = sandwichP * number

print("total cost : ",total)

