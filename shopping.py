def get_order():
    print("[command] [item] (command is a to add, d to delete, q to quit)") # (1) our order "interface"
    line = input() # (2) We can't just return the input(), we need to parse it, starting with putting it's value into a variable

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