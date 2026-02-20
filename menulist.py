#write a  program to create a list and perform various operation on list using menu


list1=[]

while True:
    print("\n----MENU----")
    print("1 Add Element")
    print("2 Delete Element")
    print("3 Display list")
    print("4 Sort list")
    print("5 Search element")
    print("6 Exit")

    choice =int(input("Enter Your choice:"))

    if choice == 1:
        item = int(input("Enter Element to add:"))
        list1.append(item)
        print("Element added")

    elif choice == 2:
        item = int(input("Enter element to delete:"))
        if item in list1:
            list1.remove(item)
            print("Element deleted")
        else:
            print("Element not found:")

    elif choice == 3:
        print("List element:",list1)

    elif choice == 4:
        list1.sort()
        print("Sorted list:",list1)

    elif choice == 5:
        item =int(input("Enter element to search:"))
        if item in list1:
            print("Element found in list:")
        else:
            print("Element not found:")

    elif choice == 6:
        print("Exiting:")
        break
    else:
        print("Invalid choice:") 
