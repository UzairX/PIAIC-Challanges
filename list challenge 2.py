def access_element(input_list, index):
    """Return the element at the specified index or an error message if out of range."""
    if index < 0 or index >= len(input_list):
        return "Index out of range."
    return input_list[index]

def modify_element(input_list, index, new_value):
    """Replace the element at the specified index with a new value or return an error message if out of range."""
    if index < 0 or index >= len(input_list):
        return "Index out of range."
    input_list[index] = new_value
    return input_list

def slice_list(input_list, start, end):
    """Return a new list containing elements from start to end index (exclusive) or an error message if indices are out of range."""
    if start < 0 or end > len(input_list) or start > end:
        return "Invalid slice indices."
    return input_list[start:end]

def main():
    my_list = [10, 'apple', 5.5, 'banana', 42]

    while True:
        print("\nCurrent list:", my_list)
        print("Select an operation:")
        print("1: Access an element")
        print("2: Modify an element")
        print("3: Slice the list")
        print("4: Exit")

        choice = input("Enter the operation number (1-4): ")

        if choice == '1':
            index = int(input("Enter the index to access: "))
            result = access_element(my_list, index)
            print("Accessed element:", result)

        elif choice == '2':
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            result = modify_element(my_list, index, new_value)
            print("Updated list:", result)

        elif choice == '3':
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            result = slice_list(my_list, start, end)
            print("Sliced list:", result)

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

main()
