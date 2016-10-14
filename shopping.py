def get_order():
    print("[command] [item] (command is a to add, d to delete, q to quit)")
    line = input()
    
    command = line[:1] # (1) line[:1] = start at sub[0], end at [1];
    item = line[2:] # (2) line[2:] = start at sub[2], end at the end of list;
    
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