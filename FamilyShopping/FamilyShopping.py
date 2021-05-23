# Single Inheritance
from ParentShopping import ParentShopping


class FamilyShopping(ParentShopping):
    familyShoppingBag = list()
    familyShoppingBag.append("Rice")
    familyShoppingBag.append("Table")
    familyShoppingBag.append("Pulse")
    familyShoppingBag.append("Sofa Cover")
    familyShoppingBag.append("Pillow")
    familyShoppingBag = list()
    familyShoppingBag.append("Rice")
    familyShoppingBag.append("Table")
    familyShoppingBag.append("Pulse")
    familyShoppingBag.append("Sofa Cover")
    familyShoppingBag.append("Pillow")

    def familyShoppingItems(self):
        return self.familyShoppingBag


# Multi Level Inheritance


