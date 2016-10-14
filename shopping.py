

def go_shopping():
  cart = []
  
    while True: 
        item = get_item()
        if item == "": 
            break 
        cart.append(item)
        
    print(cart) # (1) show the contents of the cart
    print("Finished!") # (2) explicitly tell the user we're finished
    
    
go_shopping()