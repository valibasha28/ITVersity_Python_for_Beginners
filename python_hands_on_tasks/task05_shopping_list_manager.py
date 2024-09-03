shopping_list = []

while True:
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Clear List")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print("Item added\n\n")
    elif choice == '2':
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print("Item removed.\n\n")
        else:
            print("Item not found!\n\n")
    elif choice == '3':
        print("Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f'{i}. {item}')
        print('\n\n')
    elif choice == '4':
        shopping_list.clear()
        print("Shopping List is Cleared!\n\n")
    elif choice == '5':
        print("Exited!!")
        break
    else:
        print("Invalid option, please choose a valid option.")
