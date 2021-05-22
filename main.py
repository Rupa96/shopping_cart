# Rupa goes to a super market. She buys lots of products. We have to make a bill for her shopping list.

                        # CUSTOMER
# Rupa will go the super market.
# She will pick up a basket. (So that she can collect her products.)
# She will go the billing counter.

                        # SHOPKEEPER
# First, shopkeeper will segregate the items according to their categories.
# After that, shopkeeper counts the quantity of each products.
# Multiplied qty with unit price of the products to get the final price.
# Finally adds the total price .

# Shopping bag
shoppingBag = list()
shoppingBag.append("Biscuit")
shoppingBag.append("Paneer")
shoppingBag.append("Colgate")
shoppingBag.append("Colgate")
shoppingBag.append("Coke")
shoppingBag.append("Bread")
shoppingBag.append("Bread")
shoppingBag.append("Bread")
shoppingBag.append("Milk")
shoppingBag.append("Biscuit")
shoppingBag.append("Paneer")
shoppingBag.append("Paneer")
shoppingBag.append("Paneer")
shoppingBag.append("Paneer")
shoppingBag.append("Colgate")
shoppingBag.append("Coke")
shoppingBag.append("Coke")
shoppingBag.append("Coke")
shoppingBag.append("Coke")
shoppingBag.append("Coke")
shoppingBag.append("Coke")
shoppingBag.append("Coke")
shoppingBag.append("Bread")
shoppingBag.append("Milk")
shoppingBag.append("Biscuit")
shoppingBag.append("Paneer")
shoppingBag.append("Colgate")
shoppingBag.append("Coke")
shoppingBag.append("Bread")
shoppingBag.append("Milk")
shoppingBag.append("Biscuit")
shoppingBag.append("Paneer")
shoppingBag.append("Colgate")
shoppingBag.append("Coke")
shoppingBag.append("Bread")

# Billing Counter

# Segregation of products as per their categories (To find categories of products)
productCategories = set(shoppingBag)

# Count the quantity of the products
billingDict = dict()
for category in productCategories:
    count = 0
    for item in shoppingBag:
        if category == item:
            count += 1
    billingDict[category] = count
print(billingDict)

