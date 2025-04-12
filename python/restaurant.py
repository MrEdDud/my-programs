#Displays the main menu and collects choice of menu item
def menu():

    flag = True

    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show total sales for a specific item") 
        print("2. Visual Graphs")

        main_menu_choice = input("Please enter the number of your choice (1-2): ")

        try:
            int(main_menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(main_menu_choice) < 1 or int(main_menu_choice) > 2:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(main_menu_choice)

#Menu item selection form user and validates it
def get_product_choice():

    flag = True

    while flag:
        print("######################################################")
        print("Please choose a menu item from the list:")
        print("Please enter the number of the item (1-8)")
        print("1.  Nachos")
        print("2.  Soup")
        print("3.  Burger")
        print("4.  Brisket")
        print("5.  Ribs")
        print("6.  Corn")
        print("7.  Fries")
        print("8.  Salad")
        print("######################################################")

        menu_list = ["Nachos","Soup","Burger", "Brisket","Ribs","Corn", "Fries", "Salad"]

        item_choice = input("Please enter the number of your choice (1-8): ")

        try:
            int(item_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(item_choice) < 1 or int(item_choice) > 8:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                item_name = menu_list[int(item_choice)-1]
                return item_name

#Gets user input of start of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_start_date():
    
    flag = True
    
    while flag:
        start_date = input('Please enter start date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(start_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return start_date

#Gets user input of end of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_end_date():
    
    flag = True
    
    while flag:
        end_date = input('Please enter end date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(end_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return end_date

#imports data set and extracts data and returns data for a specific menu item within a user defined range
def get_selected_item(item, startdate, enddate):
    df1 = pd.read_csv("Task4a_data.csv") 
    df2 = df1.loc[df1['Menu Item'] == item]
    df3 = df2.loc[:,startdate:enddate]

    return df3

#allows user to register an account or login into their account
def choice():
    
    flag = True

    while flag:
        choice = input("Would you like to login or register? ")
        choice = choice.casefold()
        if choice == "register" or choice == "login":
            flag = False
        else:
            flag = True

#register
    if choice == "register":
        username = input('Create a new username ')
        password = input('Create a new password ')
        print("\n")
        
        flag = True

        while flag:
            loginUsername = input("Enter your username ")
            if loginUsername == username:
                flag = False
            else:
                print("Wrong")

        flag = True

        while flag:
            loginPassword = input("Enter your password ")
            if loginPassword == password:
                flag = False
                print("\nLogin Successful")
            else:
                print("Wrong")
#login
    else:
        flag = True

        while flag:
            loginUsername = input("Enter your username ")
            if loginUsername == username:
                flag = False
            else:
                print("Wrong")

        flag = True

        while flag:
            loginPassword = input("Enter your password ")
            if loginPassword == password:
                flag = False
                print("\nLogin Successful!")
            else:
                print("Wrong")

#Graph item selection form user and validates it
def get_graph_choice():

    flag = True

    while flag:
        print("######################################################")
        print("Please choose a graph type from the list:")
        print("Please enter the number of the item (1-3)")
        print("1.  Bar Graph")
        print("2.  Scatter Chart")
        print("3.  Histogram")
        print("4.  Main Menu")
        print("######################################################")

        graph_list = ["Bar Graph","Scatter Chart","Histogram"]

        graph_choice = input("Please enter the number of your choice (1-4): ")

        try:
            int(graph_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(graph_choice) < 1 or int(graph_choice) > 4:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                graph_name = graph_list[int(graph_choice)-1]
                return graph_name

#asks the user if they want to go back to the menu
def backToMenu():
    back_to_menu = input("Would you like to go back to the menu? ")
    back_to_menu = back_to_menu.casefold()
    if back_to_menu == "yes":
        menu()
    else:
        print()

choice()
main_menu = menu()
if main_menu == 1:

    item = get_product_choice()
    start_date = get_start_date()
    end_date = get_end_date()
 
    extracted_data = get_selected_item(item, start_date, end_date)
    
    print("Here is the sales data for {} between dates {} and {}:".format(item, start_date, end_date))
    extract_no_index = extracted_data.to_string(index=False)

    print(extract_no_index)
else:
    df = pd.read_csv("Task4a_data.csv")
    graph = get_graph_choice()
    startDate = start_date = get_start_date()

    if graph == "Bar Graph":
      sns.barplot(data=df, x="Menu Item", y=startDate, hue="Service")
      plt.show

    elif graph == "Scatter Chart":
      sns.scatterplot(data=df, x="Menu Item", y=startDate, hue="Service")
      plt.show

    elif graph == "Histogram":
      sns.histplot(data=df, x="Menu Item", y=startDate, hue="Service")
      plt.show
    
    else:
        menu()
