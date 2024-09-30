use std::io;

mod quicksort;
mod bubble_sort;
mod sum;
mod login;
 Add user and hash passsword

fn main() {
let mut data = [55, 88, 77, 23, 11, 87];
    loop {
        println!("Choose a sorting method: ");
        println!("1-Add user ");
        println!("2-Bubble sort ");
        println!("3-Quicksort ");
        println!("3-Sum two numbers ");
        println!("4- print unsorted array ");
        println!("5-Exit ");

        let mut choice = String::new();
        io::stdin().read_line(&mut choice).expect("Failed to read line");

        match choice.trim(){
            "1" => login::add_user(),

            "2" => {
                bubble_sort::bubble_sort_func(&mut data);
                println!("Sorted array: {:?}", data);
            }

            "3" => {
                quicksort::quicksort_function(&mut data); 
                println!("Array sorted by quicksort: {:?}", data);
            }

            "4" => sum::add_two_numbers(),

            "5" => println!("Unsorted array: {:?}", data),

            "6" => {
                println!("Quitting...");
                break;
            },
            _ => println!("Invalid choice."),

        }
    }    
}