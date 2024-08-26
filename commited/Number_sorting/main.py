from functions import random_numbers, merge_sort, delete_data , binary_search, numbers

def main():

    is_running = True
    while is_running:
        print("1 - Add plus 10000 unsorted numbers: ")
        print("2 - Sort numbers(merge sort): ")
        print("3 - Delete all numbers:")
        print("4 - Search for a number:")
        print("5 - Exit :")

        choice = input("Choose the operation: ")

        if choice == '1':
            random_numbers()
            print(numbers)
            
        elif choice == "2":
            sorted_numbers = merge_sort(numbers)
            print(sorted_numbers)

        elif choice == '3':
            delete_data()

        elif choice == '4':
            sorted_numbers = merge_sort(numbers)

            target_input = int(input("Enter the number you want to search for: "))
            
            result = binary_search(sorted_numbers, target_input)
            
            if target_input in sorted_numbers:
                print(f"Element found at index {result}")
            else:
                print("Element not found")

        elif choice == '6':
            is_running = False

        else:
            print("Invalid option.")
    print("operation ended.")

if __name__ == '__main__':
     main()