def get_order(): # (2) change function name here too
    print("Please enter an item:")
    return input()

def go_shopping():
    cart = []
  
    while True: 
        item = get_order() # (1) raise the level of abstraction (become more generalized) for 'get_item' 
        if item == "": 
            break
        cart.append(item)
        
    print(cart)
    print("Finished!")
    
    
go_shopping()