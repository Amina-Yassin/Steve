def cashier ():
    running_total = 0
    count = 0
    more_items = True
    while more_items == True:
        item = float(input("price of item. If no more then enter 0 in place."))
        running_total = running_total + item
        count = count + 1    
        # print ("Your total so far is:", running_total)
        # print ("Total items so far is:", count)
        if item == 0:
            more_items = False
            final_count = count - 1
            f_running_total = round(running_total,2)
            avgcost = round(f_running_total/count,2)
            gst = round(f_running_total*1.05,2)

            print ("Your total items is:",final_count)
            print ("The average cost per item is:", avgcost)
            print ("Your total before GST is:", f_running_total)
            print ("And Your GRand total is:", gst)

cashregister = cashier()