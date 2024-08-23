from functions import random_numbers, merge_sort, delete_data , numbers

def main():

    is_running = True
    while is_running:
        print("1 - Add plus 10000 unsorted numbers: ")
        print("2 - Sort numbers(merge sort): ")
        print("3 - Delete all numbers:")
        print("4 - Exit :")

        choice = input("Choose the operation: ")

        if choice == '1':
            random_numbers()
            print(numbers)
            
        elif choice == "2":
            sorted_numbers = merge_sort(numbers)
            print(sorted_numbers)

        elif choice == '3':
            delete_data()

        elif choice == '6':
            is_running = False

        else:
            print("Invalid option.")
    print("operation ended.")

if __name__ == '__main__':
     main()