# The following script is dedicated to the management of Scout's equipment. Program have following options:
# show the current eq status; calculate expenses; manage item list and food list by adding and removing params;
# check the money status and possibility to buy new items/food.

# eq is dict of three params: money (starting with 120,50), items (list of items), food (list of food).

eq = {'money': 120.50, 'items': ['compass', 'flashlight', 'bedroll'], 'food': ['apple', 'water', 'bar', 'bar']}

# this function prints the whole eq without formatting


def print_eq(eq_to_print):
    print(eq_to_print)


print_eq(eq)

print("Scout bought sleeping mat which cost was 29.99.")

# modified by buying a new item

eq['money'] -= 29.99
eq['items'].append('sleeping_mat')
print_eq(eq)

# eating snack bar and modifying the eq

eq['food'].remove('bar')
print("Scout ate a bar! He ain't hungry now :)")

# printing items and food stats

eq_stats = int(len(eq['items'])) + int(len(eq['food']))
print("Scout has", eq_stats, "items and food in his/her eq.")

# function buy takes price and thing name, and eq given, and updates the new eq status.


def buy(price, thing, eq):
    print("Scout bought a map for 5.99.")
    eq['money'] -= price
    eq['items'].append(thing)


buy(5.99, 'map', eq)

# function buy v 2.0. This version checks and informs if the Scout has enough money to buy thing.


def check_buy(price, thing, eq):
    if eq['money'] > price:
        print("Scout has a money and can buy some stuff")
        eq['money'] -= price
        eq['items'].append(thing)
        print("Stuff bought!")
    else:
        print("Sory, no money to buy stuff...")
    return


check_buy(20, 'hat', eq)
check_buy(200, 'hunting_gun', eq)