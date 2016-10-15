def get_order():
    print("[command] [item] (command is a to add, d to delete, q to quit)")
    line = input()

    command = line[:1] 
    item = line[2:] 

    return command, item

def process_order(order, cart):
    command, item = order

    if command == "a":
        cart.add(item) # (2)
    elif command == "d" and item in cart:
        cart.remove(item)
    elif command == "q":
        return False

    return True

def go_shopping():
    cart = set() # (1)

    while True:
        order = get_order()

        process_order(order, cart)

        if not process_order(order, cart):
            break

    print(cart)
    print("Finished!")
    
    
go_shopping()

# 3 data structures:
alist = [ 1, 2, 3 ]
atuple = ( 1, 2, 3 ) # a tuple is essentially a list that you cannot change, you cannot add to it or remove from it
aset = set() # the built in set() function gives me an empty set
asettwo = { 1, 2, 3 } # I can init my set with say 3 numbers, and curly braces
# a set is unordered! aset.add(0) vs alist.append(0)
# a set is trying to prevent duplicate entries!
# all the values inside of a set have to be unique!
# (1) So in my program, I'll change my cart from being a list to being a set
# (2) And I'll also change append() method to add()
