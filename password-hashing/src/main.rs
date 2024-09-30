use std::io;

mod login;

fn main() {
    loop {
        println!("Choose a sorting method: ");
        println!("1-Add user ");
        println!("2-Exit ");

        let mut choice = String::new();
        io::stdin().read_line(&mut choice).expect("Failed to read line");

        match choice.trim(){
            "1" => login::hash_credentials(),

            "2" => {
                println!("Quitting...");
                break;
            },
            _ => println!("Invalid choice."),

        }
    }    
}