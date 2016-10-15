def get_order():
    print("[command] [item] (command is a to add, d to delete, q to quit)")
    line = input()

    command = line[:1] 
    item = line[2:] 

    return command, item
    
def go_shopping():
    cart = []
    

def process_order(order, cart): # (1) so process_order takes an order and a cart
    command, item = order # (2) and I can unpack them here (this is an example of usefulness of tuple)

    while True: 
        order = get_order()

        process_order(order, cart)
        if item == "": 
            break

    print(cart)
    print("Finished!")
    
    
go_shopping()


