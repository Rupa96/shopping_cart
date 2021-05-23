from FamilyShopping import ParentShopping, FamilyShopping
from KidShopping import KidShopping


class Billing:
    kidsShopping = KidShopping()
    parentShopping = ParentShopping()
    familyShopping = FamilyShopping()
    finalShoppingList = list()
    finalShoppingSet = None
    billingDict = dict()

    def generateBill(self):
        kidShoppingItems = self.kidsShopping.kidShoppingItems()
        parentShoppingItems = self.kidsShopping.parentShoppingItems()
        familyShoppingItems = self.kidsShopping.familyShoppingItems()
        self.finalShoppingList.extend(kidShoppingItems)
        self.finalShoppingList.extend(parentShoppingItems)
        self.finalShoppingList.extend(familyShoppingItems)
        self.finalShoppingSet = set(self.finalShoppingList)
        print(len(self.finalShoppingList))

        for category in self.finalShoppingSet:
            count = 0
            for item in self.finalShoppingList:
                if category == item:
                    count += 1
            self.billingDict[category] = count
        print("Final Shopping bill", self.billingDict)

    # self.parentShopping.kidShoppingItems() # parent can't access child class porperty
    # self.familyShopping.kidShoppingItems()


billing = Billing()
billing.generateBill()
