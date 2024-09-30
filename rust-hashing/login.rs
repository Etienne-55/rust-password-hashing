use std::io;

pub fn add_user() {

    let mut email = String::new();
    let mut password = String::new();

    println!("Enter email: ");
    io::stdin().read_line(&mut email).expect("Failed to read line");
    let email: i32 = email.trim().parse().expect("Error");

    println!("Enter password: ");
    io::stdin().read_line(&mut password).expect("Failed to read line");
    let password: i32 = password.trim().parse().expect("Type a password");

    
    println!("email {} password {}", email, password);
}