prices_list =[]

while True:
    #show menu to user
    print("=======Menu=======")
    print("1 - Add price")
    print("2 - Show average price")
    print("3 - Show highest price")
    print("q - quit")

    #get user input
    user_input =input("Enter your choice: ")

    if user_input=="1":
        #convert price into float
        price = float(input('Enter price to add: '))
        def add_price(prices_list,price):
            prices_list.append(price) #add prices to list
            print("prices list is ",prices_list)
        add_price(prices_list ,price )    
    elif user_input=="2":
        #show average price
        def get_average_price(prices_list):
            if(len(prices_list)>0):
                total = 0 
                for i in prices_list:
                    total = total + i
                print(total/len(prices_list))     
            else:
                print('List is empty') 
        get_average_price(prices_list)          
    elif user_input=="3":
        #find max price from list
        def get_max_price(prices_list):
            if(len(prices_list)>0):
                print(max(prices_list))
            else:
                print('List is empty') 
        get_max_price(prices_list)
    #quit the program
    elif user_input.lower()=="q":
        break
    else:
        #check correct option entered
        print("Invalid input")        
        continue
