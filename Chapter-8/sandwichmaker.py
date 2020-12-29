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

mayoP = 4
mustardP = 5
lettuceP = 7
tomatoP = 8
noP = 0

print("mayo, mustard, lettuce, or tomato?(yes/no)")
response = pyip.inputYesNo()
if response == "yes":
    a= pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'])
else:
    a = "no"
if a == 'mayo':
    ap = mayoP
elif a == 'mustard':
    aP = mustardP
elif a== 'lettuce':
    aP = lettuceP
elif a == 'tomato':
    aP = tomatoP
elif a == 'no':
    aP = noP

print("number of sandwiches required :")
number = pyip.inputInt(min = 1)
sandwichP = bprice + pprice + cPrice +aP
total = sandwichP * number

print("total cost : ",total)

