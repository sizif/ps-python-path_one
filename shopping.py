

def go_shopping():
  cart = []
  
  while True: # (1) potential infinite loop
    item = get_item()
    if item == "": # (2) if the user just presses enter
        break # (3) exit the loop
    cart.append(item)

go_shopping()