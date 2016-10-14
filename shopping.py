def get_order():
    print("[command] [item] (command is a to add, d to delete, q to quit)")
    line = input()

    command = line[:1] 
    item = line[2:] 

    return command, item # (1) return command and item in def get_order()
    
def go_shopping():
    cart = []
  
    while True: 
        order = get_order() # (2) 'order' instead of 'item' for var name in def go_shopping(), because it's a command on an item instead of just some item
        if item == "": 
            break
        cart.append(item)
        
    print(cart)
    print("Finished!")
    
    
go_shopping()


