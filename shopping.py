def get_item(): # (1) define get_item function
    print("Please enter an item:") # (2) ask the user to enter an item
    return input() # (3) return what the user entered

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