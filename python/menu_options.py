def main_menu():    
    my_list = ["Topic 1", "Topic 2", "Topic 3","Topic 4"]; y = 0; print("=-"*20, end="=\n")
    for x in range(len(my_list)):
        print(f"{x+1}. {my_list[y]}"); y += 1
    while True:
        choice = input("Enter a choice.\n> ")
        try:
            int(choice)
        except:
            print("Error: You can only choose 1, 2, 3 or 4!")
        else:
            choice = int(choice)
            if choice > len(my_list) or choice <= 0:
                print("Error: You can only choose 1, 2, 3 or 4!")
            else:
                print("=-"*20, end="=\n"); return choice
while True:
    menu = main_menu()
    if menu == 1:
        print("You entered choice 1!")
    elif menu == 2:
        print("You entered choice 2!")
    elif menu == 3:
        print("You entered choice 3!")
    else:
        print("You entered choice 4! Goodbye!"); print("=-"*20, end="=\n"); break