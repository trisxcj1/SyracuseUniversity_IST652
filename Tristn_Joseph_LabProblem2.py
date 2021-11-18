# Code
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

# a. Show the expression that gets the value of the stock dictionary at the key ‘orange’.
# Show a statement that adds an item to the stock dictionary called ‘cherry’ with some integer value and
# that adds ‘cherry’ to the prices dictionary with a numeric value.

# printing the value of the stock dictionary at the key orange
print('The value of the stock dictionary at the key orange:')
print(stock['orange'])


# added the item 'cherry' to the stock and prices dictionaries
stock['cherry'] = 9
prices['cherry'] = 0.5

for fruit in stock:
    print('Fruit:', fruit, ', stock:', stock[fruit], ', price:', prices[fruit])


# b. Write the code for a loop that iterates over the stock dictionary and prints each key and value
print('Printing each key-value pair within the stock dictionary:')
for item in stock:
    print('key:', item, ', value:', stock[item])

    
# c, Suppose that we have a list:
groceries = ['apple', 'banana', 'pear']

# Write the code that will sum the total number in stock of the items in the groceries list.
print('Finding the total available stock for the items in groceries:', groceries)
groceries_stock = 0 
for item in groceries:
    groceries_stock += stock[item]

print('The total total available stock for the items in groceries is', groceries_stock)

# d. Write the code that can print out the total value in stock of all the items. This program can
# iterate over the stock dictionary and for each item multiply the number in stock times the price
# of that item in the prices dictionary. (This can include the items for ‘cherry’ or not, as you choose.
print('Calculating the total value of all items in stock')
total_value = 0
for item in stock:
    total_value += stock[item] * prices[item]

print('The total value of all items is stock is ${:,.2f}'.format(total_value))


# Output:
# The value of the stock dictionary at the key orange:
# 32
# Fruit: banana , stock: 6 , price: 4
# Fruit: apple , stock: 0 , price: 2
# Fruit: orange , stock: 32 , price: 1.5
# Fruit: pear , stock: 15 , price: 3
# Fruit: cherry , stock: 9 , price: 0.5
# Printing each key-value pair within the stock dictionary:
# key: banana , value: 6
# key: apple , value: 0
# key: orange , value: 32
# key: pear , value: 15
# key: cherry , value: 9
# Finding the total available stock for the items in groceries: ['apple', 'banana', 'pear']
# The total total available stock for the items in groceries is 21
# Calculating the total value of all items in stock
# The total value of all items is stock is $121.50
