
print("\n* * * * FIVE DOLLAR FRIDAY * * * * \nUse coupon code 'ALEXRULES' to get all items for $5. (regular price: $10)")
print("\n\n\nWelcome to Julia's shop. \n\tEnter the items you would like to purchase. \n\tEnter 'Show' to see your current list. \n\tEnter 'Delete' to remove a single item. \n\tEnter 'Finish' to finish adding items and proceed to check out.\n")


items = []

while True:
    
    item = input("\nEnter the name of the item you'd like to purchase:    ")
    
    if item.lower() == "finish" or item.lower() == "quit":
        finish = input("\nThanks for shopping with us today! \n\tEnter 'Check Out' if are ready to check out. \n\tEnter 'Go Back' If you've changed your mind and want to continue adding items. \n\tEnter 'Quit' If you'd like to leave the store.\n\t")
        if finish.lower() == 'go back' or finish.lower() == 'goback':
            continue
        elif finish.lower() == 'check out' or finish.lower() == 'checkout':
            coupon = input("\n\tEnter the coupon code: ")
            if coupon.upper() == "ALEXRULES" or coupon.upper() == "ALEX RULES":
                price = 5
                print("\n\nCode applied!")
            else:
                price = 10
                print("\n\nCode invalid.")
            print(f"\nYour total today is ${len(items) * price}.00")
            reciept = input("\n\nWould you like a reciept? Enter Yes or No ")
            if reciept.lower() == "yes":
                print("\nRECIEPT FOR JULIA'S STORE:")
                for x in items:
                    print(f"\t --- {x.title()} --- ${price}.00")
                print(f"\t --- TOTAL: --- ${len(items) * price}.00")
                break
            else:
                break
       
        elif finish.lower() == 'quit':
            print("\nWe hope next time you find something you like!")
            break
        else:
            print("Sorry, we don't understand that command. Please continue shopping")
    
    elif item.lower() == "show":
        print("\n\tHere's your shopping cart so far:\n\t", end = "" )
        for x in items: 
            print(" -" + x.title(), end="")
        print("\n")
        

    elif item.lower() == "delete" or item.lower() == "remove":
        removed_item = input("\n\tEnter the name of the item you'd like to remove: ")
        if removed_item.lower() in items:
            items.remove(removed_item.lower())
            print(f"\tOne {removed_item} removed from cart. Enter 'Delete' to remove more items or enter your next item.")
        else:
            print("sorry, we didn't understand your input. We are redirecting you back to the store.")


    
    else:
        quan = input(f"\tEnter the quantity of {item}s: ")
        if quan == '':
            items.append(item.lower())
        else: 
            for n in range(int(quan)):
                items.append(item.lower())
    

        
print("\n\n\nThank you for visiting our store! Have a great day!\n\n\n")