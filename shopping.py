def get_order():
    print("[command] [item] (command is a to add, d to delete, q to quit)")
    line = input()

    command = line[:1] 
    item = line[2:] 

    return command, item
    
def go_shopping():
    cart = []
    
# (4) It's the job of process_order() to figure out what to add to the cart or remove from it
def process_order(order, cart):
    
    while True: 
        order = get_order()
        # (3) I'll call it process_order(), and I'll give it the order and the cart
        process_order(order, cart)
        if item == "": 
            break
        # cart.append(item)
        # (1) I can no longer just cart.append(item), I have to figure out what's in the order
        # (2) So it might be a good idea to do some top-down design and just hand this off to another function: (3) 
        
    print(cart)
    print("Finished!")
    
    
go_shopping()


