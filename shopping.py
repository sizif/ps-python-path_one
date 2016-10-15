def get_order():
    print("[command] [item] (command is a to add, d to delete, q to quit)")
    line = input()

    command = line[:1] 
    item = line[2:] 

    return command, item
    
def go_shopping():
    cart = []
    

def process_order(order, cart):
    command, item = order

    # (1) And I can do simple string comparisons on 'command' to figure out what the user wants to do:
    if command == "a":
        cart.append(item)
    elif command == "d":
        cart.remove(item)
    elif command == "q": # (2) 'q' will return False and the function will exit at this point and return the false to the while loop in go_shopping(): (3)
        return False

    while True: 
        order = get_order()

        process_order(order, cart)
        # (3) so down here I don't have to check the item anymore, instead I'll replace it with and if statement to check the return value of process_order()
        # if item == "":
        #    break

    print(cart)
    print("Finished!")
    
    
go_shopping()


