use std::io;

mod login;
use login::{add_user, hash_credentials};


fn main() {
    loop {
        println!("User id hasher using sha-256: ");
        println!("1-Add user. ");
        println!("2-Exit. ");

        let mut choice = String::new();
        io::stdin().read_line(&mut choice).expect("Failed to read line");

        match choice.trim(){
            "1" => {
                let (email, password) = add_user();
                hash_credentials(&email, &password);
            }

            "2" => {
                println!("Quitting...");
                break;
            },
            _ => println!("Invalid choice."),

        }
    }    
}