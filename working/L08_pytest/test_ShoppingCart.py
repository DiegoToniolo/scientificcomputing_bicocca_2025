from ShoppingCart import *

def test_add():
    s = ShoppingCart()
    for i in INVENTORY.keys():
        s.add(i, 1)
    for i in INVENTORY.keys():
        s.items.index(Item(i))

def test_subtotal():
    s = ShoppingCart()
    tot = 0
    for i in INVENTORY.keys():
        s.add(i, 1)
        tot += INVENTORY[i]
    
    assert s.subtotal() == tot
    
