
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            # Prompt for and add an item
            shopping_list.append(input('Enter the item to add: '))
            pass
        elif choice == '2':
            # Prompt for and remove an item
            remover = input('Enter the item to remove: ')
            if remover not in shopping_list:
                print("Item not found, try again")
            else:
                shopping_list.remove(remover)

            pass
        elif choice == '3':
            # Display the shopping list
            for i in shopping_list:
                print(i)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


print(main())
