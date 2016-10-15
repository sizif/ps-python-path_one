def get_order():
    print("[command] [item] (command is a to add, d to delete, q to quit)")
    line = input()

    command = line[:1] 
    item = line[2:] 

    return command, item

def process_order(order, cart):
    command, item = order

    if command == "a":
        cart.add(item)
    elif command == "d" and item in cart:
        cart.remove(item)
    elif command == "q":
        return False

    return True

def go_shopping():
    cart = set()

    while True:
        order = get_order()

        process_order(order, cart)

        if not process_order(order, cart):
            break

    print(cart)
    print("Finished!")
    
    
go_shopping()

# set is an UNORDERED collection of UNIQUE values
# Example:
# s1 = { 1, 2, 3 }
# s2 = { 2, 3, 4 }
# len(s1) returns '3'
# s1[0] returns 'TypeError: 'set' object does not support indexing'
# s1.difference(s2) returns '{1}', it can also be written like s1 - s2
# s1 - s2 returns {1}; s2 - s1 returns {4}
# Asking for numbes that are in both sets: s1 & s2; returns {2, 3}
# What items are in s1 or s2 but not both: s1 ^ s2; returns {1, 4}


