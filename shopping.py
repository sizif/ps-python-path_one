def get_order():
    print("[command] [item] (command is a to add, d to delete, q to quit)")
    line = input()
    
    command = line[:1] 
    item = line[2:] 
    
def go_shopping():
    cart = []
  
    while True: 
        item = get_order()
        if item == "": 
            break
        cart.append(item)
        
    print(cart)
    print("Finished!")
    
    
go_shopping()

# (i) Python Sequences (strings and lists) are used for managing a collection of items.