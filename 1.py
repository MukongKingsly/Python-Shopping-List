first_ask = input("Type the file name ending with .csv: ")
while True:
    try:
        #open file typed by user
        file = open(first_ask)
    except:
        #if file not found
        print ("No such file exists!!! Let's try again")
        first_ask = input("Type the file name ending with .csv: ")
    else:
        #got the file so go through the file to check items present
        shopping_list = file.readlines()
        file.close()    #close file after reading through lines
        shopping_dict = {}
        for shopping_line in shopping_list:
            shop_items = shopping_line.strip().split(';')   #separate indexes at ';'
            skey = shop_items[0]    #0 because the items are in the 0th index
            svalue=float(shop_items[2]) #2 because prices are in the 2nd index
            stock=int(shop_items[4])
            shopping_dict[skey] = svalue
        #display list of items found
        print ("We have: ", list(shopping_dict.keys()))
        amount_to_pay = 0
        #proceed to next questions
        s = input("Type product to buy as it is in the list but without the quotes '': ")
        if s in shopping_dict:
            while True:
                try:
                    third_ask = int(input("Type quantity to buy in figures > 0: "))
                except:
                    print ("Quantity should be a number")
                else:
                    while True:
                        amount = third_ask * svalue
                        remainder = stock - third_ask
                        #display amount to pay
                        if s=='bananas' or s=='potatoes':
                            #remainder is redefined at each while loop because a wrong value is given when program enters else loop
                            remainder = stock - third_ask
                            #if customer wants quantity that is available in stock
                            if third_ask <= stock:
                                print ("It will cost ", amount, "Euros for ", third_ask,"kilograms of ",\
                                       s, "\nThere are ", remainder,"kilograms of ", s, "left in stock")
                                break
                            else:
                                print ("Not enough stock. Your quantity should not be more than ", stock)
                                break
                        elif s=='gingerbread' or s=='coffee(400g)' or s=='beans(500g)' or s=='rice(1kg)' or \
                             s=='carrot(500g)' or s=='nutsmix(1kg)' or s=='apples(1kg)':
                            remainder = stock - third_ask
                            #if customer wants quantity that is available in stock
                            if third_ask <= stock:
                                print ("You have to pay ", amount, "Euros for ", third_ask,"packs of ",\
                                       s, "\nThere are ", remainder, "packs of ", s, "left in stock")
                                break
                            else:
                                print ("Not enough stock. Your quantity should not be more than ", stock)
                                break
                        elif s=='chocolate':
                            remainder = stock - third_ask
                            #if customer wants quantity that is available in stock
                            if third_ask <= stock:
                                print ("You have to pay ", amount, "Euros for ", third_ask,"pieces of ",\
                                       s, "\nThere are ", remainder, "pieces of ", s, "left in stock")
                                amount_to_pay += amount
                                break
                            else:
                                print ("Not enough stock. Your quantity should not be more than ", stock)
                                break
                        elif s=='beer':
                            #remainder is redefined at each while loop because a wrong value is given when program enters else loop
                            remainder = stock - third_ask
                            #if customer wants quantity that is available in stock
                            if  third_ask <= stock:
                                print ("You have to pay ", amount, "Euros for ", third_ask,"bottles of ",\
                                       s, "\nThere are ", remainder, "bottles of ", s, "left in stock")
                                break
                            else:
                                print ("Not enough stock. Your quantity should not be more than ", stock)
                                break                  
                        elif s=='mayonaise(500g)' or s=='jam(500g)':
                            remainder = stock - third_ask
                            #if customer wants quantity that is available in stock
                            if third_ask <= stock:
                                print ("You have to pay ", amount, "Euros for ", third_ask,"containers of ",\
                                       s, "\nThere are ", remainder, "containers of ", s, "left in stock")
                                break
                            else:
                                print ("Not enough stock. Your quantity should not be more than ", stock)
                                break
                        elif s=='tincorn(500g)' or s=='sardine(400g)':
                            remainder = stock - third_ask
                            #if customer wants quantity that is available in stock
                            if third_ask <= stock:
                                print ("You have to pay ", amount, "Euros for ", third_ask,"tins of ",\
                                       s, "\nThere are ", remainder, "tins of ", s, "left in stock")
                                break
                            else:
                                print ("Not enough stock. Your quantity should not be more than ", stock)
                                break
                    break
        else:
            #if wrong item typed
            print ("Item not found")
