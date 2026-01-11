from ShoppingCart import *

def test_Item_add():
    for i in INVENTORY.keys():
        a, b = Item(i, 1), Item(i, 2)
        c = a+b
        assert c.name == i
        assert c.quantity == 3
        
def test_Item_eq():
    for i in INVENTORY.keys():
        a, b = Item(i), Item(i)
        assert (a == b) == True
    
    l = list(INVENTORY.keys())
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            a, b = Item(l[i]), Item(l[j])
            assert (a == b) == False