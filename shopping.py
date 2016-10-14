def get_order():
    print("[command] [item] (command is a to add, d to delete, q to quit)")
    line = input()

    command = line[:1] 
    item = line[2:] 
    order = command, item # (i) To create a tupple (another sequence type to manage multiple items):
    # (i2) I can also create a tuple with round brackets: order = (command, item)
    # (i3) Tupple with in operator: "apples" in order 
    # the above returns True
    # (i4) Just like a list, I can say, what's offset[0], what's offset[1], like this:
    # order[0]
    # order[1]
    # a tuple is like a list, but it's faster and safer (cuz you can't append or delete from it)
    # "tuple unpacking": c,i = order
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


